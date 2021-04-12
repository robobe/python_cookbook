from msg import struct_t_pb2
from google.protobuf.struct_pb2 import Struct

m = struct_t_pb2.TestStruct()
m.data.update({"a": 1, "b": "2", })
m.data["c"] = True
m.data["d"] = [1, 2]
m.data["e"] = None
m.data["f"] = {"k1":2, "k3":4}

print(m.data["a"])
print(m.data["b"])
print(m.data["c"])
print(m.data["d"][0])
print(m.data["e"])
print(m.data["f"]["k3"])

s = Struct()
s.update({"a": 1})
print(s)
print(s.fields["a"])
print(s["a"])

