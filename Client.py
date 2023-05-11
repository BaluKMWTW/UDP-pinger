from socket import *
import time
import sys

serverAddress = ('172.20.1.98', 12000)
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

rtt = []

for i in range(1, 11):
    message = 'Ping #' + str(i)
    try:
        start = time.time()
        print('start time: ', start, 'seconds')

        clientSocket.sendto(message.encode(), (serverAddress))
        modified_message, serverAddress = clientSocket.recvfrom(2048)
        print(modified_message.decode())

        end = time.time()
        print('return time: ', end, 'seconds')

        elapsed = end - start
        rtt.append(elapsed)
        print('RTT: ', elapsed, 'seconds')

    except timeout:
        print('Ping #' + str(i) + ' request timed out\n')
clientSocket.close()
