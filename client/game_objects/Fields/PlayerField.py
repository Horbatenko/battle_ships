import random
from client.game_objects.Cells import Ship, Water
from client.game_objects.Fields.Field import Field

class PlayerField(Field):

    def __init__(self, height, width, shipsNum):
        Field.__init__(self, height, width, 'Your field: ')
        self.shipsNum = shipsNum

    def genField(self):
        self.field = []
        maxPosition = self.height * self.width
        shipsPositions = random.sample(range(0, maxPosition), self.shipsNum)
        iter = 0
        for i in range(0, self.height):
            row = []
            for j in range(0, self.width):
                if iter in shipsPositions:
                    row.append(Ship.Ship(i, j, self))
                else:
                    row.append(Water.Water(i, j, self))
                iter += 1
            self.field.append(row)