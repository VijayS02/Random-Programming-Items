import socket
import pickle
import time
import random
from tqdm import tqdm

HEADERSIZE = 10



def raw_recieve(sock):
    full_msg = b''
    header = -1
    while True:
        msg = sock.recv(32)
        if msg != b'': 
            full_msg += msg
            header = int(full_msg[:HEADERSIZE])
            if len(full_msg[HEADERSIZE:]) == header:
                return full_msg[HEADERSIZE:]

def send(msg_type, message,sock):
    request = {"type": msg_type,  "content":message}
    msg = pickle.dumps(request)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    sock.send(msg)
    # For some reason this is needed for program functionality.
    print("",end="")


def main_recieve(sock):
    message = pickle.loads(raw_recieve(sock))
    if message['type'] == "pingtest":
        ping_test(message['content'])
    elif message['type'] == "message":
        print(message['content'])
    return message

    
def ping_test(server_time):
    ping = (time.time() - server_time)*1000
    print("Ping: %3d ms" % ping)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.0.103', 1243))

    main_recieve(s)
    send("pingtest", time.time(), s)

    command = main_recieve(s)
    if command['type'] == 'command':
        command = command['content']
        if command['exec'] == 'record':
            curr = 0
            for a in range(command['iters']):
                data = []
                for i in range(a*100):
                    val = random.random()
                    curr += val
                    data.append(val)
                send('data', data, s)
            send("end", curr, s)
            print(curr)
    main_recieve(s)
    input()
