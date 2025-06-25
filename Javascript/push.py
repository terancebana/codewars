#!/usr/bin/env python3

import subprocess
import sys
import argparse
import datetime

def run_command(command, env=None):
    """Run a shell command and return True if successful, False otherwise."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True, env=env)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False

def validate_date(date_str):
    """Validate that the date string is in YYYY-MM-DD format."""
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def main():
    parser = argparse.ArgumentParser(description='Automate GitHub push with commit message and optional date')
    parser.add_argument('-m', '--message', required=True, help='Commit message')
    parser.add_argument('-d', '--date', help='Commit date in YYYY-MM-DD format (optional)', default=None)
    args = parser.parse_args()

    # Validate date format if provided
    if args.date and not validate_date(args.date):
        print("Error: Date must be in YYYY-MM-DD format")
        sys.exit(1)

    # Stage changes
    if not run_command("git add ."):
        print("Failed to stage changes")
        sys.exit(1)

    # Prepare commit command
    commit_command = f'git commit -m "{args.message}"'
    env = None
    if args.date:
        # Set environment variables for backdated commit
        commit_date = f"{args.date}T12:00:00"
        env = {
            **subprocess.os.environ,
            'GIT_AUTHOR_DATE': commit_date,
            'GIT_COMMITTER_DATE': commit_date
        }

    # Execute commit
    if not run_command(commit_command, env=env):
        print("Failed to commit changes")
        sys.exit(1)

    # Push to GitHub
    if not run_command("git push"):
        print("Failed to push to GitHub")
        sys.exit(1)

    print("Successfully pushed to GitHub!")

if __name__ == "__main__":
    main()