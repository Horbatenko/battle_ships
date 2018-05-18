from client.game_objects.Cells.Cell import Cell
from client.game_objects.Icons import ShipIcon, ShotedShipIcon as SSI

class Ship(Cell):
    def __init__(self, x, y, field):
        icon = ShipIcon.ShipIcon()
        Cell.__init__(self, icon, x, y, field)

    def onHit(self):
        newIcon = SSI.ShotedShipIcon()
        if Cell.onHit(self, newIcon):
            self.field.shipsNum -= 1