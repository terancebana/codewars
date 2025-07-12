#!/usr/bin/env python3
import subprocess
import sys
import argparse

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Automate GitHub push with commit message')
    parser.add_argument('-m', '--message', required=True, help='Commit message')
    args = parser.parse_args()

    # Stage all changes
    if not run_command("git add ."):
        print("Failed to stage changes")
        sys.exit(1)

    # Commit with message
    commit_command = f'git commit -m "{args.message}"'
    if not run_command(commit_command):
        print("Failed to commit changes")
        sys.exit(1)

    # Push to GitHub
    if not run_command("git push"):
        print("Failed to push to GitHub")
        sys.exit(1)

    print("Successfully pushed to GitHub!")

if __name__ == "__main__":
    main()