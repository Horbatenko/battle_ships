from .Connection import Connection
from .game_objects.Fields import PlayerField, EnemyField
from termcolor import colored


class Player:

    def __init__(self, host, port, fieldHeight, fieldWidth, shipsNum):
        self.connection = Connection(host, port)
        self.field = PlayerField.PlayerField(fieldHeight, fieldWidth, shipsNum)
        self.enemyField = EnemyField.EnemyField(fieldHeight, fieldWidth)
        self.turn = False
        self.lastShot = {'x': None, 'y': None}

    def run(self):
        self.connection.connect()
        self.field.genField()
        self.enemyField.genField()

        while True:
            if self.getTurn():
                break

        while True:
            self.displayFields()
            if self.turn:
                self.makeShot()
                self.shotResult()
            else:
                self.takeShot()

    def getTurn(self):
        result = self.connection.receiveData().decode('UTF-8')
        if result == 'turn':
            self.turn = True
            return True
        elif result == 'wait':
            return True
        return False

    def makeShot(self):
        self.alertMessage('Make shot: ', 'yellow')
        data = str(input())
        if '-' not in data:
            self.makeShot()
        self.lastShot['x'], self.lastShot['y'] = data.split('-')
        if self.enemyField.getCell(self.lastShot['x'], self.lastShot['y']).state:
            self.connection.sendData(data, isBytes=False)
        else:
            self.makeShot()

    def shotResult(self):
        result = self.connection.receiveData().decode('UTF-8')
        if result == 'win':
            self.alertMessage('WIN', 'green')
            self.connection.disconnect()
            exit(1)
        if result == 'miss':
            self.turn = False
        self.enemyField.getCell(self.lastShot['x'], self.lastShot['y']).onHit(result)

    def takeShot(self):
        self.alertMessage('Wait', 'yellow')
        x, y = self.connection.receiveData().decode('UTF-8').split('-')
        shipsBefore = self.field.shipsNum
        self.field.getCell(x, y).onHit()
        if not self.field.shipsNum:
            self.connection.sendData('win', isBytes=False)
            self.alertMessage('LOSE', 'red')
            self.connection.disconnect()
            exit(1)
        else:
            if shipsBefore == self.field.shipsNum:
                self.connection.sendData('miss', isBytes=False)
                self.turn = True
            else:
                self.connection.sendData('hit', isBytes=False)


    def alertMessage(self, message, color):
        print(colored(message, color))

    def displayFields(self):
        self.field.print()
        self.enemyField.print()