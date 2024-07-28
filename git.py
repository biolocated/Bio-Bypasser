import subprocess

def run_git_command(command):
    """Run a Git command and print the output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def commit_merge(commit_message):
    """Stage changes, commit the merge with the provided message, and push to the remote repository."""
    try:
        # Stage all changes
        run_git_command('git add .')

        # Commit with the provided message
        run_git_command(f'git commit -m "{commit_message}"')

        # Push changes to the remote repository
        run_git_command('git push')

        print("Merge committed and pushed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define your commit message here
    commit_message = "Merge branch 'main' of https://github.com/biolocated/Bio-Bypasser\n\nResolved merge conflicts and updated local branch with remote changes."

    # Run the commit and push process
    commit_merge(commit_message)
