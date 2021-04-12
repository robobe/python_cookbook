import multiprocessing
import socket
import time
from datetime import datetime
import struct

from msg.msg_pb2 import DemoMsg

UDP_PORT=1555
ADDR = "127.0.0.1"
TOPIC = 1000

def publisher():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(20):
        time.sleep(1/100)
        msg = DemoMsg()
        msg.id = i
        msg.name = datetime.now().strftime("%H:%M:%S.%f")
        buf = msg.SerializeToString()
        buf = struct.pack("I", TOPIC) + buf
        sock.sendto(buf, (ADDR, UDP_PORT))

def init_msg(topic):
    if topic == TOPIC:
        return DemoMsg()

def subscriber():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ADDR, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        topic, data = struct.unpack("I", data[:4]), data[4:]
        msg = init_msg(topic[0])
        msg.ParseFromString(data)
        t = datetime.now().strftime("%H:%M:%S.%f")
        print(f"msg id: {msg.id}, stime: {msg.name}, ptime: {t}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=publisher, daemon=True)
    p2 = multiprocessing.Process(target=subscriber, daemon=True)

    p1.start()
    p2.start()

    p1.join()
    p2.join()