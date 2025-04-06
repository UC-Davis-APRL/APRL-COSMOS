import socket, struct, time

UDP_IP = "192.168.88.251"
UDP_PORT = 1683

flag = 7
load_1 = 10000
load_2 = 20000
load_3 = 30000
load_4 = 40000
nottime = 42314353

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start = time.time()

for x in range(1, 100):
    test = struct.pack(">IiiiiI", flag, load_1, load_2, load_3, load_4, nottime)
        
    sock.sendto(test, (UDP_IP, UDP_PORT))
    
    end = time.time()
    print(f"{end - start} seconds elapsed, {x} packets sent")
    time.sleep(0.1)
