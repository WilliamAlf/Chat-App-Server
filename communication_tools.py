#Private Librarie
from threading import Thread
from utils.prompts import *
import encryption
from connection import Listner_Connection, Sender_Connection


class Listener :
    
    def __init__(self):
        self.connection = Listner_Connection()
        self.await_connection_thread = Thread(target=self.connection.await_connection)
    
    
    def open_socket(self, connections=1):
        self.connection.listen(connections)
        self.await_connection_thread.start()
    
    
    def listen_for_message(self):
        while True:
            received_message = self.client.recv(1024)

            if received_message:
                prompt_success("message", received_message)

            elif not received_message:
                prompt_status("chat end", "Client has disconnected")
                return self.stop_listener()                
   
    
    def stop_listener(self):
        pass
   
    
    def close_socket(self):
        self.connection.close_socket()
        del self
   
    
    def __del__(self):
        prompt_status("DEL", f"{self.__class__.__name__}-object ({id(self)}) destructed")


class Sender:
    
    def __init__(self):
        self.connection = Sender_Connection()
    
    
    def send_message(self, message):
        self.connection.send_data(message)
        
        
    def close_socket(self):
        self.connection.close_socket()
        del self
            
            
    def __del__(self):
        prompt_status("DEL", f"{self.__class__.__name__}-object ({id(self)}) destructed")

