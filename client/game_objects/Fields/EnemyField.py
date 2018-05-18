from client.game_objects.Fields.Field import Field
from client.game_objects.Cells.EnemyCell import EnemyCell

class EnemyField(Field):
    def __init__(self, height, width):
        Field.__init__(self, height, width, 'Enemy Field:')

    def genField(self):
        self.field = []
        for i in range(0, self.height):
            row = []
            for j in range(0, self.width):
                row.append(EnemyCell(i, j, self))
            self.field.append(row)