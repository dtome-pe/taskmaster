import cmd
import readline
from HTTPComm import HTTPComm
from Config import Config

class ControlShell(cmd.Cmd):


    def __init__(self):
        """We inherit from Cmd class"""
        super().__init__()

        """instantiate a httpcomm class, with port stored in config class"""
        self.http_comm : HTTPComm = HTTPComm(Config.port)

        """If test get request failed, exit"""
        if self.http_comm.http_status == 'KO':
            return
        
        """Set custom prompt and commands for printing when typing help command (?)"""
        self.prompt = 'taskmaster_client>'
        self.commands = {"start [name of process]": "start a process",
            "stop [name of process]": "stop a process",
            "restart [name of process]": "restart a process",
            "reload": "stop all processes, reload configuration file and start the new processes",
            "status": "check status of programs described in config file",
            "exit": "exit taskmaster client"}

    def run(self):
        """sets interactive prompt loop"""
        self.cmdloop()

    def do_help(self, arg):
        """Print all commands if only ? with no extra argument"""
        if not arg:
            for cmd, desc in self.commands.items():
                print(f"{cmd:<30} {desc}")
        """printing only the command specified, e.g -> ? start, to be implemented"""

    #Methos handlers for all available commands, but all of them call same send method of httpcomm class

    def do_start(self, process : str):
        if process:
            self.http_comm.send('start', process)
        else:
            print("Usage: start [process name]")

    def do_stop(self, process : str):
        if process:
            self.http_comm.send('stop', process)
        else:
            print("Usage: stop [process name]")

    def do_restart(self, process : str):
        if process:
            self.http_comm.send('restart', process)
        else:
            print("Usage: restart [process name]")
    
    def do_reload(self, arg=None):
        if not arg:
            self.http_comm.send('reload')
        else:
            print("Usage: reload")

    def do_status(self, arg=None):
        if not arg:
            self.http_comm.send('status')
        else:
            print("Usage: status")

    def do_exit(self, arg=None):
        """Exit the shell."""
        print("Exiting Taskmaster client.")
        return True  # <- this causes cmdloop() to exit
