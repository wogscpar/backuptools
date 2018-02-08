import sys
import os

from git import Repo

def search_dir(path, steps):
    repos = find_repos(path, steps+1)

def find_repos(path, steps):
    steps_  = "".join(["\t" for s in range(steps)])
    path = os.path.abspath(path)
    files = os.listdir(path)
    
    for f in files:
        subpath = os.path.join(path, f)
        if os.path.isdir(subpath):
            if (subpath.endswith(".git")):
                print("Found git in {}".format(path))
                repo = Repo(path)
                if (repo.is_dirty()):
                    print(" The repository is dirty")
                if (repo.untracked_files):
                    print(" The repository has untracked files...")
            else:
                search_dir(subpath, steps)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python find_git <path>")
        sys.exit(1)
    if (not os.path.exists(sys.argv[1])):
        print("Path {} does not exist!".format(sys.argv[1]))
        sys.exit(1)
    repos = find_repos(sys.argv[1], 0)
