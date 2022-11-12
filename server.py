import socket

connections = []

#Bug - passwrods must be successfulyl sent for program to work

#Listener
knownport = 50002

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("", 55555))

clients = {}

while True:
    new_password, new_addr = socket.recvfrom(1024)
    print(f"connection from {new_addr}")
    
    clients[new_addr] = new_password
    
    socket.sendto(b"success", new_addr)
    
    for addr, password in clients.items():
        if new_password == password:
            socket.sendto((addr[0], addr[1], knownport), new_addr)
            socket.sendto((new_addr[0], new_addr[1], knownport), addr)
            