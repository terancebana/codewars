import json
import os
import random
import subprocess
import urllib.request
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

# --- Config ---
load_dotenv()
BASE_DIR = Path(__file__).parent
POOL_FILE = BASE_DIR / "kata_pool.json"
SOLVED_FILE = BASE_DIR / "solved.json"
SOLUTIONS_DIR = BASE_DIR / "solutions"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = os.getenv("GITHUB_USER")
GITHUB_REPO = os.getenv("GITHUB_REPO")


# --- Step 1: Check if already pushed today ---
def already_pushed_today():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/commits?per_page=1"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        },
    )
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if not data:
                return False
            last_commit_date = data[0]["commit"]["author"]["date"][:10]
            return last_commit_date == str(date.today())
    except Exception as e:
        print(f"[error] could not check GitHub: {e}")
        return False


# --- Step 2: Load pool and filter solved ---
def load_pool():
    with open(POOL_FILE, "r") as f:
        pool = json.load(f)

    if SOLVED_FILE.exists():
        with open(SOLVED_FILE, "r") as f:
            solved = json.load(f)
        solved_slugs = {entry["slug"] for entry in solved}
    else:
        solved_slugs = set()

    remaining = [k for k in pool if k["slug"] not in solved_slugs]

    if len(remaining) < 3:
        print(f"[warning] only {len(remaining)} kata left, add more to kata_pool.json")
        return None

    return remaining


# --- Step 3: Pick 3 random kata ---
def pick_kata(pool):
    return random.sample(pool, 3)


# --- Step 4: Fetch full kata details from Codewars API ---
def fetch_kata_details(slug):
    url = f"https://www.codewars.com/api/v1/code-challenges/{slug}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"[error] could not fetch kata '{slug}': {e}")
        return None


# --- Step 5: Solve with Gemini CLI ---
def solve_with_gemini(kata):
    name = kata.get("name", "Unknown")
    description = kata.get("description", "No description available")
    rank = kata.get("rank", {}).get("name", "unknown rank")

    prompt = f"""Solve this coding kata in Python.
Return ONLY the solution code, no explanations, no markdown backticks, no extra text.
The code must be clean, readable, and correct.

Kata Name: {name}
Rank: {rank}
Description:
{description}

Write the complete Python solution below:"""

    try:
        result = subprocess.run(
            ["gemini", "-p", prompt], capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            print(f"[error] gemini failed for '{name}': {result.stderr}")
            return None
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print(f"[error] gemini timed out for '{name}'")
        return None
    except Exception as e:
        print(f"[error] could not run gemini for '{name}': {e}")
        return None


# --- Step 6: Write solution to file ---
def write_solution(kata, solution):
    today = str(date.today())
    day_dir = SOLUTIONS_DIR / today
    day_dir.mkdir(parents=True, exist_ok=True)

    # turn kata name into a safe filename
    slug = kata.get("slug", "unknown")
    rank = kata.get("rank", {}).get("name", "unknown rank")
    # turns "7 kyu" into "7kyu"
    rank_prefix = rank.replace(" ", "")
    filename = f"{rank_prefix}_python_{slug.replace('-', '_')}.py"
    filepath = day_dir / filename

    rank = kata.get("rank", {}).get("name", "unknown rank")
    url = f"https://www.codewars.com/kata/{slug}"

    header = f"""# Kata: {kata.get("name", "Unknown")}
# Rank: {rank}
# Solved: {today}
# Source: {url}
# -----------------------------------------------

"""
    with open(filepath, "w") as f:
        f.write(header + solution)

    print(f"[info] wrote solution: {filepath}")
    return filepath


# --- Step 7: Git add, commit, push ---
def git_push(today):
    try:
        subprocess.run(["git", "add", "."], cwd=BASE_DIR, check=True)
        subprocess.run(
            ["git", "commit", "-m", f"solved 3 kata - {today}"],
            cwd=BASE_DIR,
            check=True,
        )
        subprocess.run(
            ["git", "push", "--set-upstream", "origin", "master"],
            cwd=BASE_DIR,
            check=True,
        )
        print("[info] pushed to github successfully")
    except subprocess.CalledProcessError as e:
        print(f"[error] git operation failed: {e}")


# --- Step 8: Update solved.json ---
def update_solved(picked):
    today = str(date.today())

    if SOLVED_FILE.exists():
        with open(SOLVED_FILE, "r") as f:
            solved = json.load(f)
    else:
        solved = []

    for kata in picked:
        solved.append({"slug": kata["slug"], "name": kata["name"], "solved_on": today})

    with open(SOLVED_FILE, "w") as f:
        json.dump(solved, f, indent=2)

    print(f"[info] updated solved.json with {len(picked)} new entries")


# --- Main ---
def main():
    print(f"[info] starting codewars-auto - {date.today()}")

    # step 1: check if already done today
    if already_pushed_today():
        print("[info] already pushed today, going back to sleep")
        return

    # step 2 & 3: load pool and pick 3
    pool = load_pool()
    if pool is None:
        print("[error] not enough kata in pool, exiting")
        return

    picked = pick_kata(pool)
    print(f"[info] picked kata: {[k['name'] for k in picked]}")

    # step 4, 5, 6: fetch, solve, write
    successfully_solved = []
    for kata in picked:
        print(f"[info] processing: {kata['name']}")

        # fetch full details from codewars
        details = fetch_kata_details(kata["slug"])
        if details is None:
            print(f"[warning] skipping '{kata['name']}' due to fetch error")
            continue

        # solve with gemini
        solution = solve_with_gemini(details)
        if solution is None:
            print(f"[warning] skipping '{kata['name']}' due to gemini error")
            continue

        # write to file
        write_solution(details, solution)
        successfully_solved.append(kata)

    # only push if at least something was solved
    if not successfully_solved:
        print("[error] no kata were solved successfully, not pushing")
        return

    # step 7 & 8: push and update solved.json
    update_solved(successfully_solved)
    git_push(str(date.today()))

    print(f"[info] done. solved {len(successfully_solved)}/3 kata today")


if __name__ == "__main__":
    main()
