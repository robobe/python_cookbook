import multiprocessing
import zmq
import time

def rep():
    
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print('Binding to port 5555')
    message = socket.recv()
    print(f"Received request: {message}")
    time.sleep(1)
    socket.send(b"Message Received")

def req():
    time.sleep(1)
    context = zmq.Context()
    print("Connecting to Server on port 5555")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5555")
    print('Sending Hello')
    socket.send(b"Hello")
    print('Waiting for answer')
    message = socket.recv()
    print(f"Received: {message}")

if __name__ == "__main__":
    p_req = multiprocessing.Process(target=req)
    p_rep = multiprocessing.Process(target=rep)
    p_rep.start()
    p_req.start()

    p_req.join()
    p_rep.join()
