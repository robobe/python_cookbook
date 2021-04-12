from msg import msg_pb2

p = msg_pb2.DemoMsg()
p.id = 1
p.name = "demo 1"
buf = p.SerializeToString()
pp = msg_pb2.DemoMsg()
pp.ParseFromString(buf)
print (pp)
