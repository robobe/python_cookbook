# Use black, mypy, pylint and other to code like pro

## Black
Format python code automatically

```
pip install black
```

### usage
```bash
black <file or folder to format>
# check only 
black --check <file or folder to format>
```

### VSCode config
```json
"editor.formatOnSave": true,
"editor.formatOnPaste": true,
"python.formatting.provider": "black",
??
"python.formatting.blackArgs": [
    "-t",
    "py37"
]
```
&nbsp;  
&nbsp;  
## mypy
Mypy is a static type checker to check python annotations

```
pip install mypy
```

### usage
```bash
mypy <filename>.py
```

## pylint
Python code analysis

```
pip install pylint
```

### VSCode
```json
"python.linting.pylintEnabled": true
```

### .pylintrc
Add `.pylintrc` to control lint 

for example: disabled missing docstring
```ini
[MASTER]
disable=
    C0114, # (missing-module-docstring)
    C0115  # (missing-class-docstring)
```

### control lint in code
Disabled on specific line

```python
@dataclass
class Point3D:
    x: int                  # pylint: disable=invalid-name
    y: int
    z: int
```

lint still warning `invalid-name` on `y,z` variable

## Tools to check
- bandit
- 
## Reference
- [Use black, mypy, and pylint to make your Python code more professional](https://medium.com/codex/use-black-mypy-and-pylint-to-make-your-python-code-more-professional-b594512f4362)