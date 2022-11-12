import socket

server_ip = "192.168.66.3"
server_port = 55555

server = (server_ip, server_port)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("", 50001))
socket.sendto(b"pass", server)

while True:
    data = socket.recv(1024).decode()
    
    if data.strip() == "success":
        print("checked in with server, waiting")
        break
    

ip, sport, dport = socket.recv(1024).decode()

print("\nGot Peer")
print(f"\tip: {ip}")
print(f"\tsource port: {sport}")
print(f"\tdest port: {dport}\n")

  