import socket, struct, time

UDP_IP = "127.0.0.1"
#UDP_IP = "10.0.0.51"
UDP_PORT = 1682

flag = 0
nottime = 69
nitroT = 1
keroInj = 2
loxInj = 3
keroMani = 4
loxMani = 5
keroFlow = 6
loxFlow = 7
enginePress = 8
loadCell_A = 9
loadCell_B = 10
thermocouple_A = 11
thermocouple_B = 12

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start = time.time()

for x in range(1, 100):
    test = struct.pack("IIIIIIIIII", flag, nottime, nitroT, keroInj, loxInj, keroMani, loxMani, keroFlow, loxFlow, enginePress)
        
    sock.sendto(test, (UDP_IP, UDP_PORT))
    
    end = time.time()
    print(f"{end - start} seconds elapsed, {x} packets sent")
    time.sleep(0.1)
