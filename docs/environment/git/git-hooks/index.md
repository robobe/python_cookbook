---
title: GIT hooks
tags:
    - git
    - hooks
---
Git hooks are scripts that Git executes automatically every time particular event occures in a Git repository.  
Every Git repository has a `.git/hooks` folder with a script for each hook you can bind to.  


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

```

### Commit VSCode
![](/img/git_hook_vs_alert.png)

!!! Warning
    Don't forget to assign executable permission
## References
- [githooks](https://githooks.com/)
- [Get Started with Git Hooks](https://medium.com/@f3igao/get-started-with-git-hooks-5a489725c639)
- [Raise the Bar of Code Quality in Python Projects](https://levelup.gitconnected.com/raise-the-bar-of-code-quality-in-python-projects-7c49743f004f)