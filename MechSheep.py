import Animal
import defines
import SosHogweed
import Ground
import Collisions
import Plant


class MechSheep(Animal.Animal):
    def __init__(self, world, x, y, strength=defines.MECHSHEEP_STRENGTH):
        super().__init__(world, x, y, strength, initiative=defines.MECHSHEEP_INIT, name=defines.MECHSHEEP_NAME)

    def Replicate(self, posOfParentX, posOfParentY):
        newOrgPosX, newOrgPosY = self.SearchForFreePos(posOfParentX, posOfParentY)
        if newOrgPosX > -1 and self.GetAge() > 5 and self._world.board[posOfParentX][posOfParentY].GetAge() > 5:
            self.SetAge(0)
            self._world.board[posOfParentX][posOfParentY].SetAge(0)
            newOrg = MechSheep(self._world, newOrgPosX, newOrgPosY)
            self._world.AddOrg(newOrg)
            self._world.board[newOrgPosX][newOrgPosY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozmnozyl sie")

    def IsSameSpecies(self, defender):
        if isinstance(defender, MechSheep):
            return True
        else:
            return False

    def Action(self):
        if SosHogweed.SosHogweed.counter != 0:
            minVal = 10000
            index = 0
            tmpIndex = 0
            for i in self._world.organisms:
                if isinstance(i, SosHogweed.SosHogweed):
                    tmpVal = abs(i.GetPosX() - self.GetPosX())
                    tmpVal += abs(i.GetPosY() - self.GetPosY())
                    if tmpVal < minVal:
                        minVal = tmpVal
                        index = tmpIndex
                tmpIndex += 1
            xOfTarget = self._world.organisms[index].GetPosX()
            yOfTarget = self._world.organisms[index].GetPosY()

            newPosX = self.GetPosX()
            newPosY = self.GetPosY()
            if abs(xOfTarget - self.GetPosX()) > abs(yOfTarget - self.GetPosY()):
                if xOfTarget > self.GetPosX():
                    newPosX = self.GetPosX() + 1
                else:
                    newPosX = self.GetPosX() - 1
            else:
                if yOfTarget > self.GetPosY():
                    newPosY = self.GetPosY() + 1
                else:
                    newPosY = self.GetPosY() - 1
        else:
            while True:
                newPosX, newPosY = self.RandomisePos(self.GetPosX(), self.GetPosY())
                if self._world.CheckIfIsBounds(newPosX, newPosY):
                    break

        defender = self._world.board[newPosX][newPosY]
        if self.IsSameSpecies(defender):
            self.Replicate(defender.GetPosX(), defender.GetPosY())
            self._world.AddToLogs(self.GetName() + " rozmnozyl sie")
        elif not isinstance(defender, Ground.Ground) and isinstance(defender, Animal.Animal):
            self._world.AddToLogs(self.GetName() + " atakuje " + defender.GetName())
            self.DecodeCollision(defender.Collision(self), newPosX, newPosY)
        elif not isinstance(defender, Ground.Ground) and isinstance(defender, Plant.Plant):
            self._world.AddToLogs(self.GetName() + " zjada " + defender.GetName())
            self.DecodeCollision(defender.Collision(self), newPosX, newPosY)
        else:
            self.DecodeCollision(Collisions.Collisions.MOVE, newPosX, newPosY)

    def Color(self):
        return '#66ffff'
