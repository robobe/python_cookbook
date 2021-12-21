from dataclasses import dataclass, asdict

@dataclass
class Point3D:
    x:int
    y:int
    z:int


point_3d = Point3D(1,2,3)
print(point_3d)
d_data = asdict(point_3d)
print(d_data)