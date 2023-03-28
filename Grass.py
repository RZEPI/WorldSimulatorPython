import Plant
import defines


class Grass(Plant.Plant):
    def __init__(self, world, x, y, strength=defines.GRASS_STRENGTH, initiative=defines.PLANT_INIT, name=defines.GRASS_NAME):
        super().__init__(world, x, y, strength, initiative, name)

    def Replicate(self, x, y):
        newX, newY = self.SearchForFreePos(x, y)
        if newX > -1:
            newOrg = Grass(self._world, newX, newY)
            self._world.AddOrg(newOrg)
            self._world.board[newX][newY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozsial sie")

    def Color(self):
        return '#66ff99'
