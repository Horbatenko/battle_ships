from client.game_objects.Cells.Cell import Cell
from client.game_objects.Icons import WaterIcon, ShotedWaterIcon as SWI

class Water(Cell):

    def __init__(self, x, y, field):
        icon = WaterIcon.WaterIcon()
        Cell.__init__(self, icon, x, y, field)

    def onHit(self):
        newIcon = SWI.ShotedWaterIcon()
        Cell.onHit(self, newIcon)
