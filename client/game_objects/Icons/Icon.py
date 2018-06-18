from termcolor import colored


class Icon:

    def __init__(self, sign, color):
        self.sign = sign
        self.color = color

    def display(self):
        print(colored(self.sign, self.color), end=' ')