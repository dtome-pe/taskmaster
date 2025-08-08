import cmd
import readline
from HTTPComm import HTTPComm

class ControlShell(cmd.Cmd):

    #We inherit from Cmd class, and then set custom prompt and commands for printing when typing "??
    def __init__(self, http_comm : HTTPComm):
        super().__init__()
        self.http_comm = http_comm
        self.prompt = 'taskmaster_client>'
        self.commands = {"start [name of process]": "start a process",
            "stop [name of process]": "stop a process",
            "restart [name of process]": "restart a process",
            "reload": "stop all processes, reload configuration file and start the new processes",
            "status": "check status of programs described in config file",
            "exit": "exit taskmaster client"}

    def run(self):
        #interactive prompt loop
        self.cmdloop()

    def do_help(self, arg):
        #print commands if only "?"
        if not arg:
            for cmd, desc in self.commands:
                print(f"{cmd:<30} {desc}")
        #to be implemented printing only the command specified, e.g -> ? start

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
