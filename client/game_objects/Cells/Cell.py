from abc import ABC, abstractmethod


class Cell(ABC):

    @abstractmethod
    def __init__(self, icon, x, y, field):
        self.icon = icon
        self.x = x
        self.y = y
        self.field = field
        self.state = True

    def display(self):
        self.icon.display()

    def onHit(self, newIcon):
        if self.state:
            self.icon = newIcon
            self.state = False
            return True
        else:
            return False