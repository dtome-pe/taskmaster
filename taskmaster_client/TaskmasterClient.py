from HTTPComm import HTTPComm
from ControlShell import ControlShell

class TaskmasterClient:
    
    def __init__(self, port):
        self.http_comm : HTTPComm = HTTPComm(port)
        if self.http_comm.http_status == 'KO':
            return
        self.control_shell : ControlShell = ControlShell()