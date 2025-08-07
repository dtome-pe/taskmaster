from TaskmasterClient import TaskmasterClient
import sys

def main():
    if (len(sys.argv) != 2):
        print("Wrong number of arguments")
        sys.exit(1)

    print(sys.argv[1])
    task_client : TaskmasterClient = TaskmasterClient(sys.argv[1])


if __name__ == "__main__":
    main()