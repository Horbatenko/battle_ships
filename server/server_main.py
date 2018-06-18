from server.Server import Server
from config import ServerConfig as SC


def main():
    server = Server(SC.host, SC.port)
    server.run()


if __name__ == '__main__':
    main()