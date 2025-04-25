# MiniGit
MiniGit is a basic version control system built in python. It mimics some of the fetures of git, allowing you to initialize a repository, stage files, commit changes, and view commit history.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/emanntahirr/MiniGit.git
2. Make sure you have Python 3.x installed on your machine. You can check if you have Python installed by running the following command:
   ```bash
   python3 --version
3. Navigate to project directory:
   ```bash
   cd MiniGit
## Usage
1. Initialise a repository:
   To create a new repository, run the following command:
   ```bash
   python minigit.py init
2. Add files to staging area:
   To add files to the staging area, use the command:
   ```bash
   python minigit.py add <filename>
3. Commit changes with a message:
   To commit staged changes, use the following command with a message:
   ```bash
   python minigit.py commit -m "commit message"
4. View commit history:
   To see the commit history, use:
   ```bash
   python minigit.py log
## Coding Style
- Python code is written following PEP 8 guidelines.
- Code is modular and functions are named with snake_case
- Constants are written in UPPERCASE
## Test
- There are no formal unit tests set up at this time.
- The functionality can be manually tested by using various commands (init, add, commit, log) and ensuring they work as expected.
## License
This project is licensed under the MIT license 
   
