import os
from git import Repo, GitCommandError

def clone_repo(repo_url, clone_dir):
    """
    Clone a remote repository to a local directory.
    """
    try:
        repo = Repo.clone_from(repo_url, clone_dir)
        print(f"Cloned repository from {repo_url} to {clone_dir}")
        return repo
    except GitCommandError as e:
        print(f"Error during cloning: {e}")
        return None

def get_repo_status(repo):
    """
    Print the status of the repository.
    """
    try:
        status = repo.git.status()
        print("Repository status:")
        print(status)
    except Exception as e:
        print(f"Error getting status: {e}")

def list_branches(repo):
    """
    List all branches in the repository.
    """
    print("Local branches:")
    for branch in repo.branches:
        print(f" - {branch}")

def create_branch(repo, branch_name):
    """
    Create a new branch and check it out.
    """
    try:
        # Create a new branch (head)
        new_branch = repo.create_head(branch_name)
        # Check out the new branch
        new_branch.checkout()
        print(f"Created and checked out new branch: {branch_name}")
        return new_branch
    except GitCommandError as e:
        print(f"Error creating branch: {e}")

def add_and_commit(repo, file_path, commit_message):
    """
    Stage a file and commit the changes.
    """
    try:
        # Add file to the staging area
        repo.index.add([file_path])
        # Commit the changes
        repo.index.commit(commit_message)
        print(f"Committed changes: '{commit_message}'")
    except GitCommandError as e:
        print(f"Error committing changes: {e}")

def push_changes(repo, remote_name='origin', branch_name='master'):
    """
    Push commits to the specified remote and branch.
    """
    try:
        remote = repo.remote(name=remote_name)
        push_info = remote.push(branch_name)
        print(f"Pushed changes to {remote_name}/{branch_name}")
        # Optionally, inspect push_info for details
    except GitCommandError as e:
        print(f"Error pushing changes: {e}")

def pull_changes(repo, remote_name='origin', branch_name='master'):
    """
    Pull the latest changes from the remote repository.
    """
    try:
        remote = repo.remote(name=remote_name)
        pull_info = remote.pull(branch_name)
        print(f"Pulled changes from {remote_name}/{branch_name}")
    except GitCommandError as e:
        print(f"Error pulling changes: {e}")

def main():
    # Replace with your actual repository URL and desired local directory
    repo_url = "https://github.com/your_username/your_repo.git"
    clone_dir = "local_repo"

    # Clone the repository
    repo = clone_repo(repo_url, clone_dir)
    if repo is None:
        return

    # Get repository status
    get_repo_status(repo)

    # List local branches
    list_branches(repo)

    # Create and switch to a new branch called "new_feature"
    branch_name = "new_feature"
    create_branch(repo, branch_name)
    list_branches(repo)

    # Create a new file and commit it
    new_file = os.path.join(clone_dir, "new_file.txt")
    with open(new_file, "w") as f:
        f.write("This is a new file created to demonstrate GitPython.\n")
    add_and_commit(repo, new_file, "Add new_file.txt for demonstration")

    # Push the new branch (or changes) to the remote repository
    push_changes(repo, branch_name=branch_name)

    # (Optional) Pull latest changes from remote
    # pull_changes(repo, branch_name=branch_name)

if __name__ == "__main__":
    main()
