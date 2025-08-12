import subprocess
import sys
from pathlib import Path
import random
import string

REPO_PATH = Path("C:/Users/alexs/IdeaProjects/working-activity")  # <-- Change this!
FILE_NAME = "filetopush.txt"
FILE_CONTENT = "This is a file created by a Python script.\n"
COMMIT_MESSAGE = "Add or update example.txt"
BRANCH = "main"
REMOTE = "origin"

def generate_random_string(length):
    """Generates a random alphanumeric string of a specified length."""
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        sys.exit(result.returncode)
    return result.stdout.strip()

def main():
    file_path = REPO_PATH / FILE_NAME
    file_path.write_text(FILE_CONTENT + generate_random_string(50))
    
    run(f"git add {file_path.name}", cwd=REPO_PATH)
    run(f'git commit -m "{COMMIT_MESSAGE}"', cwd=REPO_PATH)
    run(f"git push {REMOTE} {BRANCH}", cwd=REPO_PATH)
    print("Checked in.")

if __name__ == "__main__":
    main()
