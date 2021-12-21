# Dataclass Dict relations

## convert DC to Dict and back
- asdict method: convert D.C to dict
- unpack: init dataclass with unpack dict into __init__ method
- [acite package](#dacite): simplifies creation of data classes (PEP 557) from dictionaries.
- 
### asdict
using builtin method

```python
{{include("/home/user/projects/python_cookbook/dataclasess_cook/dc_2_dict.py")}}

# Result
dataclass: Point3D(x=1, y=2, z=3)
Dict: {'x': 1, 'y': 2, 'z': 3}
```

### unpack
```python
{{include("/home/user/projects/python_cookbook/dataclasess_cook/dict_2_dc.py")}}

# Result
Dict: {'x': 1, 'y': 2, 'z': 3}
Dataclass: Point3D(x=1, y=2, z=3)
```

## dacite

[package github](https://github.com/konradhalas/dacite)

```
pip install dacite
```

- Demo using nested with optional
- More examples in github repo
  
```python
{{include("/home/user/projects/python_cookbook/dataclasess_cook/dacite_demo.py")}}

# Result
B(a=A(x='test', y=1))
B(a=A(x='test', y=None))
```