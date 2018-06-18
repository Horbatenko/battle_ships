from client.Player import Player
from config import ServerConfig as SC, FieldConfig as FC


def main():
    player = Player(SC.host, SC.port, FC.height, FC.width, FC.shipsNum)
    player.run()


if __name__ == '__main__':
    main()