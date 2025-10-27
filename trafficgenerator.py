import socket, struct, time
import numpy as np

UDP_IP = "127.0.0.1"
UDP_PORT = 1683

flag = 7
load_1 = [10000] * 10
load_2 = [20000] * 10
load_3 = [30000] * 10
load_4 = [40000] * 10
nottime = 42314353


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start = time.time()

for x in range(1, 100):

    test = struct.pack("<I10i10i10i10iI", flag, *load_1, *load_2, *load_3, *load_4, nottime)
        
    sock.sendto(test, (UDP_IP, UDP_PORT))
    
    end = time.time()
    print(f"{end - start} seconds elapsed, {x} packets sent")
    time.sleep(0.1)
