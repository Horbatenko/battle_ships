from ..Cells.Water import Water
from termcolor import colored
from abc import ABC, abstractmethod


class Field(ABC):

    @abstractmethod
    def __init__(self, height, width, label):
        self.height = height
        self.width = width
        self.label = colored(label, 'grey', attrs=['underline'])
        self.field = []

    def genField(self):

        for i in range(0, self.height):
            row = []
            for j in range(0, self.width):
                row.append(Water(i, j, self))
            self.field.append(row)

    def print(self):
        print(self.label)
        for row in self.field:
            for cell in row:
                cell.display()
            print()

    def getCell(self, x, y):
        try:
            cell = self.field[int(x)][int(y)]
        except IndexError:
            return self.field[0][0]
        else:
            return cell