import random

import Plant
import Collisions
import defines


class Guarana(Plant.Plant):
    def __init__(self, world, x, y, strength=defines.GUARANA_STRENGTH, initiative=defines.PLANT_INIT, name=defines.GUARANA_NAME):
        super().__init__(world, x, y, strength, initiative, name)

    def Replicate(self, x, y):
        newX, newY = self.SearchForFreePos(x, y)
        if newX > -1:
            newOrg = Guarana(self._world, newX, newY)
            self._world.AddOrg(newOrg)
            self._world.board[newX][newY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozsial sie")

    def Collision(self, attacker):
        self.Die()
        return Collisions.Collisions.GUARANA_BOOST

    def Color(self):
        return '#3366ff'
