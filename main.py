from TestServer import TestServer
import sys

def main():
    test_server = TestServer(int(sys.argv[1]))

if __name__ == "__main__":
    main()