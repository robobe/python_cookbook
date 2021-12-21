from dataclasses import dataclass

@dataclass
class Point3D:
    x: int                  # pylint: disable=invalid-name
    y: int
    z: int


point_data = {"x": 1, "y": 2, "z": 3}

point_3d = Point3D(**point_data)
print(point_data)
print(point_3d)
