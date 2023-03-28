import random

import Plant
import Collisions
import Ground
import defines


class Milt(Plant.Plant):
    def __init__(self, world, x, y, strength=defines.MILT_STRENGTH, initiative=defines.PLANT_INIT, name=defines.MILT_NAME):
        super().__init__(world, x, y, strength, initiative, name)

    def Replicate(self, x, y):
        newX, newY = self.SearchForFreePos(x, y)
        if newX > -1:
            newOrg = Milt(self._world, newX, newY)
            self._world.AddOrg(newOrg)
            self._world.board[newX][newY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozsial sie")

    def Action(self):
        i = 0
        while i != defines.TRIES_OF_MILT_REPLICATION:
            randNum = random.randint(0, defines.CHANCE_FOR_PLANT_TO_REPLICATE)
            if randNum == 1:
                self.Replicate(self.GetPosX(), self.GetPosY())
                break
            i += 1

    def Color(self):
        return '#ffff00'
