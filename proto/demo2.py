from msg import msg2_pb2
from google.protobuf.struct_pb2 import Value

p = msg2_pb2.DemoMsg2()
p.id = 1
p.data.update({"f1": 1, "f2": "string", "f3": True, "f4": None})
buf = p.SerializeToString()
pp = msg2_pb2.DemoMsg2()
pp.ParseFromString(buf)

print (pp.data.fields["f1"].number_value)
print (pp.data.fields["f2"].string_value)
print (pp.data.fields["f3"])
print (pp.data.fields["f4"])
print(type(pp.data.fields["f3"]))
print(dir(Value))