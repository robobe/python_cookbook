from dataclasses import dataclass
from typing import Optional
from dacite import from_dict

@dataclass
class A:
    x: str
    y: Optional[int]


@dataclass
class B:
    a: A


data = {
    'a': {
        'x': 'test',
        'y': 1,
    }
}

data_opt = {
    'a': {
        'x': 'test'
    }
}

result = from_dict(data_class=B, data=data)
print(result)
result = from_dict(data_class=B, data=data_opt)
print(result)