#!/bin/bash

# list merged branches
BRANCHES=`git branch -r --merged | grep -v "*" | grep -v master | grep -v develop | grep -v release/ | grep -v hotfix/ | sed 's/origin\///'`
printf "Removing branches: \n$BRANCHES"

# delete all remote branches merged into the current branch (i.e. develop), excluding release/master/develop branches
git branch -r --merged | grep -v "*" | grep -v master | grep -v develop | grep -v release/ | grep -v hotfix/ | sed 's/origin\///' | xargs -n 1 git push --delete origin
