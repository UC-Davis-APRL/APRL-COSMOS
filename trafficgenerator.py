import socket, struct, time

UDP_IP = "127.0.0.1"
#UDP_IP = "10.0.0.51"
UDP_PORT = 1683

flag = 7
nottime = 69
nitroT = 30000
keroInj = 30000
loxInj = 30000
keroMani = 30000
loxMani = 30000
keroFlow = 30000
loxFlow = 30000
enginePress = 30000
loadCell_A = 2413342
loadCell_B = 1234321
loadCell_C = 2314343
loadCell_D = 2348678
thermocouple_A = 11
thermocouple_B = 12

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start = time.time()

for x in range(1, 100):
    #test = struct.pack(">IIIIIIIIII", flag, nottime, nitroT, keroInj, loxInj, keroMani, loxMani, keroFlow, loxFlow, enginePress)
    test = struct.pack(">IIIIII", flag, loadCell_A, loadCell_B, loadCell_C, loadCell_D, nottime)

    sock.sendto(test, (UDP_IP, UDP_PORT))
    
    end = time.time()
    print(f"{end - start} seconds elapsed, {x} packets sent")
    time.sleep(0.1)
