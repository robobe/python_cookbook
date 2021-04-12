import multiprocessing
import zmq
import time
import msgpack

TOPIC = b"topic"

def pub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")
    print('Binding to port 5555')
    while True:
        data = msgpack.packb([1,2,3])
        socket.send_multipart((TOPIC, data))
        time.sleep(1)
        

def sub():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:5555")
    socket.setsockopt(zmq.SUBSCRIBE, TOPIC)
    while True:
        topic, data = socket.recv_multipart()
        data = msgpack.unpackb(data)
        print(data)

if __name__ == "__main__":
    p_pub = multiprocessing.Process(target=pub)
    p_sub = multiprocessing.Process(target=sub)
    p_sub.start()
    p_pub.start()

    p_pub.join()
    p_sub.join()