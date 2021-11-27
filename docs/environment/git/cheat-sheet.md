---
title: GIT cheat sheet
tags:
    - git
    - tips
---

### update local list of remote branches
```
git remote update origin --prune
```

### Change prompt to show git current branch
```
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\] \[\033[33;1m\]\w\[\033[m\] (\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)) \$
```
- `\033[0m`: No Color  
- `\033[36m`: Cyan  
- `\033[33;1m`: Yellow  
- \u\: user  
- \w\: pwd  

![](/img/ps1.png)

!!! Note
    ```
    Black        0;30     Dark Gray     1;30
    Red          0;31     Light Red     1;31
    Green        0;32     Light Green   1;32
    Brown/Orange 0;33     Yellow        1;33
    Blue         0;34     Light Blue    1;34
    Purple       0;35     Light Purple  1;35
    Cyan         0;36     Light Cyan    1;36
    Light Gray   0;37     White         1;37
    ```