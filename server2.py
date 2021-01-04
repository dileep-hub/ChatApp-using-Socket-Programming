import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "192.168.1.4"
port = 5678

s.bind((ip, port))

print()
print("\t\t\t Welcome to My CLI CHAT APP ")
print()
cip = input("enter ip: ")

while True:
s.sendto(input("\n\t\t\t\t\tMe: ").encode(), (cip , 1234))
x = s.recvfrom(100)
data = x[0].decode()
clientip = x[1][0]
print(clientip+ " [Dileep]" + " : " + data)


# s.sendto(\t\t\t\tinput("Me: ").encode(), ("192.168.1.4", 1234))
