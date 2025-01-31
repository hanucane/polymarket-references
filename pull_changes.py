import os
import subprocess

def pull_changes_from_git():
    for root, dirs, files in os.walk('.'):
        if '.git' in dirs:
            print(f"Pulling changes in {root}")
            subprocess.run(['git', '-C', root, 'pull'])

if __name__ == "__main__":
    pull_changes_from_git()