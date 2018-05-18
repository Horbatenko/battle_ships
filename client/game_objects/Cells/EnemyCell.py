from client.game_objects.Cells.Cell import Cell
from client.game_objects.Icons import WaterIcon, ShotedShipIcon as SSI, ShotedWaterIcon as SWI

class EnemyCell(Cell):

    def __init__(self, x, y, field):
        icon = WaterIcon.WaterIcon()
        Cell.__init__(self, icon, x, y, field)

    def onHit(self, hitResult):
        if hitResult == 'hit':
            newIcon = SSI.ShotedShipIcon()
        elif hitResult == 'miss':
            newIcon = SWI.ShotedWaterIcon()

        Cell.onHit(self, newIcon)