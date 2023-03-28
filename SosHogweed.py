import random

import Plant
import Animal
import MechSheep
import Collisions
import Ground
import defines


class SosHogweed(Plant.Plant):
    counter = 0

    def __init__(self, world, x, y, strength=defines.SOSHOGWEED_STRENGTH, initiative=defines.PLANT_INIT, name=defines.SOSHOGWEED_NAME):
        SosHogweed.counter = SosHogweed.counter + 1
        super().__init__(world, x, y, strength, initiative, name)


    def Replicate(self, x, y):
        newX, newY = self.SearchForFreePos(x, y)
        if newX > -1:
            newOrg = SosHogweed(self._world, newX, newY)
            self._world.AddOrg(newOrg)
            self._world.board[newX][newY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozsial sie")

    def Action(self):
        randNum = random.randint(0, defines.CHANCE_FOR_PLANT_TO_REPLICATE)
        if randNum == 1:
            self.Replicate(self.GetPosX(), self.GetPosY())

        for i in range(-1, 2):
            for j in range(-1, 2):
                tmpOrg = self._world.board[self.GetPosX()+j][self.GetPosY()+i]
                if isinstance(tmpOrg, Animal.Animal) and not isinstance(tmpOrg, MechSheep.MechSheep):
                    self._world.AddToLogs(tmpOrg.GetName() + " znalazl sie w zasiegu barszczu sosnowskiego")
                    self._world.board[tmpOrg.GetPosX()][tmpOrg.GetPosY()] = Ground.Ground(self._world, tmpOrg.GetPosX(), tmpOrg.GetPosY())
                    tmpOrg.Die()

    def Collision(self, attacker):
        if isinstance(attacker, MechSheep.MechSheep):
            self.Die()
            SosHogweed.counter = SosHogweed.counter - 1
            return Collisions.Collisions.MOVE
        else:
            self._world.board[self.GetPosX()][self.GetPosY()] = Ground.Ground(self._world, self.GetPosX(), self.GetPosY())
            self.Die()
            return Collisions.Collisions.DIE

    def Color(self):
        return '#ff0000'

