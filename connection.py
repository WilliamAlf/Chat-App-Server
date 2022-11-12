from utils.prompts import *
import socket


class Connection(object):
    has_connection = False
    
    def __init__(self, port="8080", ip="", protocol_type=socket.SOCK_STREAM):
        
        self.port = port
        self.ip = ip
        
        #Create socket by protocol type
        if protocol_type == socket.SOCK_DGRAM:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        elif protocol_type == socket.SOCK_STREAM:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    def close_socket(self):
        if self.has_connection:
            self.socket.close()
        del self
        
    
    def __del__(self):
        prompt_status("DEL", f"{self.__class__.__name__}-object ({id(self)}) destructed")


class Listner_Connection(Connection):
    
    def __init__(self, port=8080, ip="", protocol_type=socket.SOCK_STREAM):
        super().__init__(port, ip, protocol_type)
        self.socket.bind((self.ip, self.port))        


    def socket_listen(self, connections=1):
        self.socket.listen(connections)
    
    
    def await_connection(self):
        self.client, self.address = self.socket.accept()
        self.has_connection = True


class Sender_Connection(Connection):
    
    
    def __init__(self, port="9090", ip="", protocol_type=socket.SOCK_STREAM):
        super().__init__(port, ip, protocol_type)
    
    
    def connect_to_client(self):
        connection_success, connection_fail = (True, False)
        
        try:
            self.socket.connect((self.ip, self.port))        
            
        except Exception as exception:
            print(f"{self} Failed to connect to {self.ip}, Exception {exception}")
            self.has_connection = connection_fail
            return self.has_connection
            
        else:
            self.has_connection = connection_success
            return self.has_connection 

    
    def send_data(self, data):
        self.socket.sendall(data)