class InvalidCommand(Exception):
    
    def __init__(self, command):
        self.name = self.__class__.__name__
        self.command = command
        
    def toString(self):
        return f" [{self.name}] Command \"{self.command}\" not found, try again"