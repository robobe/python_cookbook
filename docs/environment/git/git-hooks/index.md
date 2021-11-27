---
title: GIT hooks
tags:
    - git
    - hooks
---
Git hooks are scripts that Git executes automatically every time particular event occures in a Git repository.  
Every Git repository has a `.git/hooks` folder with a script for each hook you can bind to.  

## Client side most common used

| Hook Name | Event | Description |
| :-------: | :---: | :---------- |
| pre-commit| git commit | Call before commit<br> exiting with anything other the zero |
| post-merge | git merge | Call after merge |
| post-checkout | git checkout <br> git clone | Run hook after updating the worktree or after git clone |



!!! Tip
    Add `.git`  folder to VSCode
    ```
    files.exclude": {
        "**/.git": false
    }
    ```


## Samples
### Minimal BASH
- Place file name `pre-commit` in `.git/hook` folder
- Assign executable permission
- if script return error (!=0) commit cancel
- if script return 0 commit allowed

```
#!/bin/bash

#!/bin/bash

echo -e "git failed to commit"

exit 1
```

### Minimal Python
```python
#!/usr/bin/env python3

print("git failed to commit")

exit(1)
```

### Hook demo
Implement python script that check if json file can parse using `json.tool` python model
- implement as pre-commit hook

```
python -m json.tool <file name>
```

- json file `demo.json` with error
```json
{
    "line1": 1,
    "line2": 2,
}
```

- run json.tool
```bash
python -m json.tool demo.json 
#
Expecting property name enclosed in double quotes: line 4 column 1 (char 34)

```

### check json 

### Commit VSCode
![](/img/git_hook_vs_alert.png)

!!! Warning
    Don't forget to assign executable permission  
    `chmod +x .git/hook/pre-commit`
## References
- [githooks](https://githooks.com/)
- [Get Started with Git Hooks](https://medium.com/@f3igao/get-started-with-git-hooks-5a489725c639)
- [Raise the Bar of Code Quality in Python Projects](https://levelup.gitconnected.com/raise-the-bar-of-code-quality-in-python-projects-7c49743f004f)