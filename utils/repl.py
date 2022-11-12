from utils.exceptions import InvalidCommand
from utils.prompts import *


def start_repl(obj):
    
    while True:
        print_commands(obj.command_list)
        
        input_command = input("Command> ")
        print("")
        
        if input_command == "exit":
            return stop_program(obj)
        else: 
            try: 
                match(obj, input_command)

            except InvalidCommand as ex:
                prompt_error(ex)  


def print_commands(commands_list):
        print("\n", "Commands:")
        for i in range(len(commands_list)):
            print(f"{i+1}. {commands_list[i]}")
            
        print("")


def match(obj, input_command):
    
    def menu_match(input_command):
        
        match input_command.lower():
            case "start chat" | "sc":
                prompt_status("command found", "starting chat")
                obj.start_chat()
            
            case "start server" | "ss":
                prompt_status("command found", "starting server")
                obj.start_server()
            
            case default:
                raise InvalidCommand(input_command)
    
    
    def chat_match():
        
        match input_command.lower():
                
            case "send message" | "sm":
                prompt_status("command found", "leaving chat")
                # *insert function call*
            
            case default:
                raise InvalidCommand 
            
    class_name = obj.__class__.__name__
    
    if (class_name == "Main"):
        menu_match(input_command)
            
    elif (class_name == "Chat"):
        chat_match(input_command)
        
        
def stop_program(obj):
    class_name = obj.__class__.__name__
    
    if class_name == "Main":
        return obj.stop_program()
    elif class_name == "Chat":
        return obj.stop_chat()