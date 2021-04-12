import multiprocessing
import zmq
import time

TOPIC = "topic"

def pub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")
    print('Binding to port 5555')
    while True:
        socket.send_string(TOPIC, zmq.SNDMORE)
        socket.send_pyobj([1,2,3])
        time.sleep(1)
        

def sub():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:5555")
    socket.setsockopt_string(zmq.SUBSCRIBE, TOPIC)
    while True:
        topic = socket.recv_string()
        data = socket.recv_pyobj()
        print(data)

if __name__ == "__main__":
    p_pub = multiprocessing.Process(target=pub)
    p_sub = multiprocessing.Process(target=sub)
    p_sub.start()
    p_pub.start()

    p_pub.join()
    p_sub.join()