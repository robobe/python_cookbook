import multiprocessing
import zmq
import time

def rep():
    
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
    print('Binding to port 5555')
    while True:
        message = socket.recv_string()
        print(f"Received request: {message}")
        time.sleep(1)
        socket.send(b"Message Received")

def req():
    time.sleep(1)
    context = zmq.Context()
    print("Connecting to Server on port 5555")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5556")
    time.sleep(1)
    for i in range(100):
        msg = f"send: {i}"
        print(f'Sending Hello {i}')
        socket.send_string("f")
        message = socket.recv()
    
if __name__ == "__main__":
    p_req = multiprocessing.Process(target=req)
    p_rep = multiprocessing.Process(target=rep)
    p_rep.start()
    p_req.start()

    p_req.join()
    p_rep.join()
