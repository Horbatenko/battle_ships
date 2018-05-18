from client.game_objects.Icons.Icon import Icon
from termcolor import cprint

class WaterIcon(Icon):

    def __init__(self):
        Icon.__init__(self, '_', 'grey')
        self.bg = 'on_blue'

    def display(self):
        cprint(self.sign, self.color, self.bg, end=' ')
