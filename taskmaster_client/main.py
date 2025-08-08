from ControlShell import ControlShell
import sys

def main():
    if (len(sys.argv) != 2):
        print("Wrong number of arguments")
        sys.exit(1)

    ControlShell().run()


if __name__ == "__main__":
    main()