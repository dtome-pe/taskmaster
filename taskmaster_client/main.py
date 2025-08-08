from ControlShell import ControlShell
from Config import Config
import sys

def main():
    if (len(sys.argv) != 2):
        print("Wrong number of arguments")
        sys.exit(1)

    Config.parse(sys.argv[1])
    if not Config.ok:
        return

    control_shell = ControlShell()
    if control_shell.status == "KO":
        return
    control_shell.run()

if __name__ == "__main__":
    main()