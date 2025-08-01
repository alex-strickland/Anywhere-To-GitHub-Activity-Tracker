import subprocess
import sys
from pathlib import Path
import random

# === CONFIGURATION ===
REPO_PATH = Path("C:/Users/alexs/IdeaProjects/working-activity")  # <-- Change this!
FILE_NAME = "filetopush.txt"
FILE_CONTENT = "This is a file created by a Python script.\n"  # Random content for uniqueness
COMMIT_MESSAGE = "Add or update example.txt"
BRANCH = "main"  # or "main", "develop", etc.
REMOTE = "origin"

def generate_random_string(length):
    """Generates a random alphanumeric string of a specified length."""
    characters = string.ascii_letters + string.digits  # Includes uppercase, lowercase, and digits
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

    # 1. Write or update file
    file_path.write_text(FILE_CONTENT + generate_random_string(50))

    # 2. Stage the file
    run(f"git add {file_path.name}", cwd=REPO_PATH)

    # 3. Commit the change
    run(f'git commit -m "{COMMIT_MESSAGE}"', cwd=REPO_PATH)

    # 4. Push to GitHub
    run(f"git push {REMOTE} {BRANCH}", cwd=REPO_PATH)

    print("Checked in.")

if __name__ == "__main__":
    main()
