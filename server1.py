import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


ip = "192.168.1.2"
port = 1234

s.bind( (ip, port) )
print()
print("\t\t\tWelcome to My CLI CHAT APP")
print()

while True:
    x = s.recvfrom(100)

    data = x[0].decode()   #to convert byte into string


    clientip = x[1][0]

    print(clientip+ " (JACK)" + "  :  " +  data)
    # print(os.system(data))

    s.sendto(input("\n\t\t\t\tMe: ").encode(), ("192.168.1.4" , 5678))
