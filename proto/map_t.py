from msg.map_msg_pb2 import DemoMap
from msg.map_msg_pb2 import Demo2Map
from msg.map_msg_pb2 import DemoData

msg = DemoMap()
msg.map1[1] = "a"
msg.map1[2] = "b"
buf = msg.SerializeToString()

msg_out = DemoMap()
msg_out.ParseFromString(buf)
print(f"print key:1: {msg_out.map1[1]}")

for k in msg_out.map1.keys():
    print(f"print key: {k}")

for v in msg_out.map1.values():
    print(f"print val: {v}")

for k, v in msg_out.map1.items():
    print(f"print key: {k} val: {v}")

k_list = msg_out.map1.keys()
print(len(k_list))

msg = Demo2Map()
inner = DemoData()
inner.f1 = 1
inner.f2 = "data"

msg.map1["key1"].CopyFrom(inner) 
print(msg.map1["key1"].f1)