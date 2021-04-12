import multiprocessing
import zmq
import time

def pull():
    
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://127.0.0.1:5556")
    print('Binding to port 5555')
    while True:
        message = socket.recv_pyobj()
        print(f"Received: {message}")
        

def push():
    time.sleep(1)
    context = zmq.Context()
    print("Connecting to Server on port 5555")
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://*:5556")
    for i in range(100):
        msg = f"send: {i}"
        socket.send_pyobj([i])
    
if __name__ == "__main__":
    p_push = multiprocessing.Process(target=push)
    p_pull = multiprocessing.Process(target=pull)
    p_pull.start()
    p_push.start()

    p_push.join()
    p_pull.join()
