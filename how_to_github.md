git stash
git stash save "Your descriptive message here"
git checkout main  # Or git checkout develop, etc.
git pull origin main  # Or git pull origin develop, etc.
git checkout your-branch-name
git stash list

# git stash appy
git stash apply  # Applies the most recent stash (stash@{0})

# Or, apply a specific stash:
git stash apply stash@{1} # Replace stash@{1} with the correct index

git stash drop  # Drops the most recent stash

# Or, drop a specific stash:
git stash drop stash@{1} # Replace stash@{1} with the correct index





git pull



