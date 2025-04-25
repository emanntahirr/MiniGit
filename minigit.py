import os 
import hashlib
import json
import sys
import datetime

MINIGIT_DIR = ".minigit"
STAGING_FILE = os.path.join(MINIGIT_DIR, "staging_area.json")
COMMITS_FILE = os.path.join(MINIGIT_DIR, "commits.json")
FILE_TRACKER_FILE = os.path.join(MINIGIT_DIR, "file_tracker.json")

def get_file_hash(file_path):
    hash_sha1 = hashlib.sha1()

    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_sha1.update(chunk)
        return hash_sha1.hexdigest()
    except Exception as e:
        print(f"Error reading file{file_path}: {e}")
        return None

def init():
    if not os.path.exists(MINIGIT_DIR):
        os.mkdir(MINIGIT_DIR)
        with open(STAGING_FILE, "w") as f:
            json.dump([], f)
        with open(COMMITS_FILE, "w") as f:
            json.dump([], f)
        print("Initialised empty MiniGit repository.")
    else:
        print("MiniGit repository already exists.")

def add(filename):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return
    
    with open(STAGING_FILE, "r") as f:
        staging_area = json.load(f)

    with open(FILE_TRACKER_FILE, "r") as f:
        file_tracker = json.load(f)

    current_hash = get_file_hash(filename)
    if current_hash is None:
        print(f"Error tracking {filename}.")
        return

    if filename not in staging_area:
        staging_area.append(filename)

    if filename not in file_tracker or file_tracker[filename] != current_hash:
        file_tracker[filename] = current_hash

    with open(STAGING_FILE, "w") as f:
        json.dump(staging_area, f)

    with open(FILE_TRACKER_FILE, "w") as f:
        json.dump(file_tracker, f)

    print(f"Added '{filename}' to staging area.")

def commit(message):
    with open(STAGING_FILE, "r") as f:
        staging_area = json.load(f)

    if not staging_area:
        print("Nothing to commit.")
        return
    
    commit_data = {}
    for filename in staging_area:
        with open(filename, "r") as f:
            content = f.read()
            commit_data [filename] = content

    commit_hash = hashlib.sha1((json.dumps(commit_data) + message).encode()).hexdigest()
    timestamp = datetime.datetime.now().isoformat()

    with open(COMMITS_FILE, "r") as f:
        commits = json.load(f)

    commits.append({
        "hash": commit_hash,
        "message": message,
        "timestamp": timestamp,
        "files": commit_data
    })

    with open(COMMITS_FILE, "w") as f:
        json.dump(commits, f, indent=4)

    with open(STAGING_FILE, "w") as f:
        json.dump([], f)

    print(f"Committed as {commit_hash[:7]}: {message}")


def log():
    with open(COMMITS_FILE, "r") as f:
        commits = json.load(f)

    for commit in reversed(commits):
        print(f"Commit {commit['hash'][:7]}")
        print(f"Date: {commit['timestamp']}")
        print(f"Message: {commit['message']}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python minigit.py <command> [args]")
        return

    command = sys.argv[1]

    if command == "init":
        init()
    elif command == "add":
        if len(sys.argv) < 3:
            print("Specify file to add.")
        else:
            add(sys.argv[2])
    elif command == "commit":
        if "-m" in sys.argv:
            message_index = sys.argv.index("-m") + 1
            message = sys.argv[message_index]
            commit(message)
        else:
            print("Commit message required. Use -m.")
    elif command == "log":
        log()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()

    