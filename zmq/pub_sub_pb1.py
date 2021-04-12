import multiprocessing
import zmq
import time
from msg_pb2 import camera_prop

TOPIC = b"topic"

def pub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")
    print('Binding to port 5555')
    while True:
        msg = camera_prop()
        msg.name = "camera1"
        msg.width = 640
        msg.height = 480
        data = msg.SerializeToBytes()
        socket.send_multipart((TOPIC, data))
        time.sleep(1)
        

def sub():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:5555")
    socket.setsockopt(zmq.SUBSCRIBE, TOPIC)
    while True:
        topic, data = socket.recv_multipart()
        msg = camera_prop()
        data = msg.FromBytes(data)
        print(type(msg))
        print(msg)

if __name__ == "__main__":
    p_pub = multiprocessing.Process(target=pub)
    p_sub = multiprocessing.Process(target=sub)
    p_sub.start()
    p_pub.start()

    p_pub.join()
    p_sub.join()