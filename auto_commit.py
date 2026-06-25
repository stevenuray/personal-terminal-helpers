#!/usr/bin/env python3

import subprocess

from datetime import datetime

def get_changed_files():
    result = subprocess.run(["git", "diff", "--name-only", "HEAD"], capture_output=True, text=True, check=True)
    return result.stdout.strip().splitlines()

def build_commit_message_from_iso8601_dt(iso8601_dt: datetime, changed_files: str) -> str:
    dt = iso8601_dt.isoformat()
    changed_files_str = ", ".join(changed_files)
    return f"Auto commit on {dt} with changes to: {changed_files_str}"

def git_add_all():
    subprocess.run(["git", "add", "."], check=True)

def git_commit(commit_msg: str):
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

def git_push():
    subprocess.run(["git", "push"], check=True)

git_add_all()
changed_files = get_changed_files()
commit_msg = build_commit_message_from_iso8601_dt(datetime.now(), changed_files)

print(f"Changed files: {changed_files}")
print(f"Commit message: {commit_msg}")

git_commit(commit_msg)
git_push()

