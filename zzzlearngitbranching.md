# drakeredwind01s_resume

forever and always run 
<details>
  <summary>git pull</summary>
  TODO:get def 
  </details>
<details>
  <summary>git status</summary>
    show modified files in working directory, staged for your next commit
    </details>
<details>
  <summary>git add [file]</summary>
    add a file as it looks now to your next commit (stage)
    </details>
<details>
  <summary>git commit</summary>
    TODO: need to add
    </details>
<details>
  <summary>git commit -m "FILE MESSAGE"</summary>
    TODO: need to add
    </details>
<details>
  <summary>git push</summary>
    Pushes your local changes to a remote repository.
    </details>


<br>
<br>
<details>
  <summary>git rebase [BRANCH]</summary>
    moves wherever head is to where you mention
    </details>


<br>
<br>


<details>
  <summary>git reset [file]</summary>
git reset [file]
  > unstage a file while retaining the changes in working directory
</details>
<details>
  <summary>git diff</summary>
git diff
  > diff of what is changed but not staged
</details>
<details>
  <summary>git diff --staged</summary>
    &nbsp;&nbsp; git diff --staged
    <br> &nbsp;&nbsp; > diff of what is staged but not yet commited
    </details>
<details>
  <summary>git commit -m “[descriptive message]”</summary>
    &nbsp;&nbsp; git commit -m “[descriptive message]”
    <br> &nbsp;&nbsp; commit your staged content as a new commit snapshot
    </details>
<details>
  <summary>git reset “[file name]”</summary>
    This command removes the specified file from the staging area, but keeps the changes in your working directory.
    </details>



| Command                     | Description                                                                                                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git pull                    | Fetches changes from a remote repository and merges them into your local branch.                                                                                         |
| git status                  | Shows the current state of your working directory and staging area, including modified, staged, and untracked files.                                                     |
| git add [file]              | Stages a file for the next commit, adding it to the staging area.                                                                                                        |
| git reset [file]            | Unstages a file, removing it from the staging area but keeping the changes in your working directory.                                                                    |
| git diff                    | Shows the differences between your working directory and the last committed version.                                                                                     |
| git diff --staged           | Shows the differences between the staged files and the last committed version.                                                                                           |
| git commit -m "[message]"`  | Creates a new commit with the staged changes and the specified message.                                                                                                  |
| git reset --hard            | Reverts all changes in your working directory and staging area to the last committed version. **Caution:** Use this command with care as it can discard unsaved changes. |
| git checkout [branch]       | Switches to a different branch, potentially discarding uncommitted changes in your current branch.                                                                       |
| git branch                  | Lists all branches in the repository.                                                                                                                                    |
| git branch [new-branch]     | Creates a new branch.                                                                                                                                                    |
| git merge [branch]          | Merges the specified branch into your current branch.                                                                                                                    |
| git log                     | Shows the commit history of the current branch.                                                                                                                          |
| git remote                  | Lists remote repositories associated with your local repository.                                                                                                         |
| git remote add [name] [url] | Adds a new remote repository.                                                                                                                                            |
| git push [remote] [branch]  | Pushes your local changes to a remote repository.                                                                                                                        |
| git clone [url]             | Creates a local copy of a remote repository.                                                                                                                             |
| git stash                   | Temporarily saves your uncommitted changes so you can switch branches or work on something else.                                                                         |

| Command                                                        | Description                                                                                                                          |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Main                                                           |                                                                                                                                      |
| Introduction Sequence                                          |                                                                                                                                      |
| A nicely paced introduction to the majority of git commands    |                                                                                                                                      |
| 1: Introduction to Git Commits                                 | git commit<br>git commit                                                                                                             |
| 2: Branching in Git                                            | git branch bugFix<br>git checkout bugFix                                                                                             |
| 3: Merging in Git                                              | git branch bugFix<br>git checkout bugFix<br>git commit<br>git checkout main<br>git commit<br>git merge bugFix                        |
| 4: Rebase Introduction                                         | git branch bugFix<br>git checkout bugFix<br>git commit<br>git checkout main<br>git commit<br>git checkout bugFix<br>git rebase main  |
| Ramping Up                                                     |                                                                                                                                      |
| The next serving of 100% git awesomes-ness. Hope you're hungry |                                                                                                                                      |
| 1: Detach yo' HEAD                                             |                                                                                                                                      |
| 2: Relative Refs (^)                                           |                                                                                                                                      |
| 3: Relative Refs #2 (~)                                        |                                                                                                                                      |
| 4: Reversing Changes in Git                                    |                                                                                                                                      |
| Moving Work Around                                             |                                                                                                                                      |
| "Git" comfortable with modifying the source tree :P            |                                                                                                                                      |
| 1: Cherry-pick Intro                                           |                                                                                                                                      |
| 2: Interactive Rebase Intro                                    |                                                                                                                                      |
| A Mixed Bag                                                    |                                                                                                                                      |
| A mixed bag of Git techniques, tricks, and tips                |                                                                                                                                      |
| 1: Grabbing Just 1 Commit                                      |                                                                                                                                      |
| 2: Juggling Commits                                            |                                                                                                                                      |
| 3: Juggling Commits #2                                         |                                                                                                                                      |
| 4: Git Tags                                                    |                                                                                                                                      |
| 5: Git Describe                                                |                                                                                                                                      |
| Advanced Topics                                                |                                                                                                                                      |
| For the truly brave!                                           |                                                                                                                                      |
| 1: Rebasing over 9000 times                                    |                                                                                                                                      |
| 2: Multiple parents                                            |                                                                                                                                      |
| 3: Branch Spaghetti                                            |                                                                                                                                      |
| Remote                                                               |                                                                                                                                      |
| Push & Pull -- Git Remotes!                                                               |                                                                                                                                      |
| Time to share your 1's and 0's kids; coding just got social                                                               |                                                                                                                                      |
| 1: Clone Intro                                                             |                                                                                                                                      |
| 2: Remote Branches                                                              |                                                                                                                                      |
| 3: Git Fetchin'                                                               |                                                                                                                                      |
| 4: Git Pullin'                                                               |                                                                                                                                      |
| 5: Faking Teamwork                                                               |                                                                                                                                      |
| 6: Git Pushin'                                                               |                                                                                                                                      |
| 7: Diverged History                                                               |                                                                                                                                      |
| 8: Locked Main                                                               |                                                                                                                                      |
| To Origin And Beyond -- Advanced Git Remotes!                                                               |                                                                                                                                      |
| And you thought being a benevolent dictator would be fun...                                                               |                                                                                                                                      |
| 1: Push Main!                                                               |                                                                                                                                      |
| 2: Merging with remotes                                                               |                                                                                                                                      |
| 3: Remote Tracking                                                               |                                                                                                                                      |
| 4: Git push arguments                                                               |                                                                                                                                      |
| 5: Git push arguments -- Expanded!                                                               |                                                                                                                                      |
| 6: Fetch arguments                                                               |                                                                                                                                      |
| 7: Source of nothing                                                               |                                                                                                                                      |
| 8: Pull arguments                                                               |                                                                                                                                      |

git rebase -i
git cherry-pick


git checkout main
git cherry-pick bugFix



We will re-order the commits so the one we want to change is on top with git rebase -i
We will git commit --amend to make the slight modification
Then we will re-order the commits back to how they were previously with git rebase -i
Finally, we will move main to this updated part of the tree to finish the level (via the method of your choosing)




| Command                     | Description                                                                             |
|-----------------------------|-----------------------------------------------------------------------------------------|
| git merge bugFix                    | ![git_merge_bugFix.png](..\Free-time-coding\z_git_commands_images\git_merge_bugFix.png) |



- [ ] git branch
- [ ] git commit
- [ ] git 
- [ ] Moving upwards one commit at a time with ^
- [ ] Moving upwards a number of times with ~<num>
- [ ] git branch -f main HEAD^
- move branch main reletive of head or
- git branch (forced) "main", to head up
- [ ] 

 social      | URL                                                                         |
-------------|-----------------------------------------------------------------------------|
 website 	 | www.redwind01.com                                                           |
 ---         | https://redwind01.wixsite.com/redwind01                                     |
 youtube 	 | https://www.youtube.com/channel/UCnw2fREws9T-1YL8m2pWGLg?sub_confirmation=1 |
 twitch:     | https://www.twitch.tv/redwind01                                             |
 discord: 	 | https://discord.gg/WbcWqVq                                                  |
 Linkedin 	 | https://www.linkedin.com/in/drake-redwind-36815512a/                        |
 facebook 	 | https://www.facebook.com/drake.redwind.73/                                  |
 twitter 	 | https://twitter.com/drakeredwind011                                         |
 instagram   | https://www.instagram.com/drakeredwind01.insta/                             |

## work I'm looking for
I'm ideally looking for a job that is in `remote full time cybersecurity`. 

I'm willing to work my way up to the top and start at $40k/y

but in this industry work can be found for $100k/y

I'm also willing to work as a `remote IT`, `remote sys admin`






a

a

a

a

a

a

d









<details>
  <summary>Click me</summary>
  
  ### Heading
  1. Foo
  2. Bar
     * Baz
     * Qux

  ### Some Javascript
  ```js
  function logSomething(something) {
    console.log('Something', something);
  }
  ```
</details>






