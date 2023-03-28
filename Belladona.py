import random

import Plant
import Collisions
import Ground
import defines


class Belladona(Plant.Plant):
    def __init__(self, world, x, y, strength=defines.BELLADONNA_STRENGTH, initiative=defines.PLANT_INIT, name=defines.BELLADONNA_NAME):
        super().__init__(world, x, y, strength, initiative, name)

    def Replicate(self, x, y):
        newX, newY = self.SearchForFreePos(x, y)
        if newX > -1:
            newOrg = Belladona(self._world, newX, newY)
            self._world.AddOrg(newOrg)
            self._world.board[newX][newY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozsial sie")

    def Collision(self, attacker):
        self._world.board[self.GetPosX()][self.GetPosY()] = Ground.Ground(self._world, self.GetPosX(), self.GetPosY())
        self.Die()
        return Collisions.Collisions.DIE

    def Color(self):
        return '#ff9900'
