for k in $(git branch -r | sed /\*/d); do 
  if [ -z "$(git log -1 --since='Aug 10, 2016' -s $k)" ]; then
    branch_name_with_no_origin=$(echo $k | sed -e "s/origin\///")
    echo branch to be deleted: $branch_name_with_no_origin
    git push origin --delete $branch_name_with_no_origin
  fi
done
