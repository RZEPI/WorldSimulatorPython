import Animal
import defines
import Ground
import Plant
import Collisions


class Fox(Animal.Animal):
    def __init__(self, world, x, y, strength=defines.FOX_STRENGTH):
        super().__init__(world, x, y, strength, initiative=defines.FOX_INIT, name=defines.FOX_NAME)

    def Replicate(self, posOfParentX, posOfParentY):
        newOrgPosX, newOrgPosY = self.SearchForFreePos(posOfParentX, posOfParentY)
        if newOrgPosX > -1 and self.GetAge() > 5 and self._world.board[posOfParentX][posOfParentY].GetAge() > 5:
            self.SetAge(0)
            self._world.board[posOfParentX][posOfParentY].SetAge(0)
            newOrg = Fox(self._world, newOrgPosX, newOrgPosY)
            self._world.AddOrg(newOrg)
            self._world.board[newOrgPosX][newOrgPosY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozmnozyl sie")

    def Action(self):
        while True:
            tmpx, tmpy = self.RandomisePos(self.GetPosX(), self.GetPosY())
            if self._world.CheckIfIsBounds(tmpx, tmpy):
                defender = self._world.board[tmpx][tmpy]
                if self.IsSameSpecies(defender):
                    self.Replicate(defender.GetPosX(), defender.GetPosY())
                    self._world.AddToLogs(self.GetName() + " rozmnozyl sie")
                elif not isinstance(defender, Ground.Ground) and isinstance(defender, Animal.Animal):
                    if defender.GetStrength() > self.GetStrength():
                        continue
                    else:
                        self._world.AddToLogs(self.GetName() + " atakuje " + defender.GetName())
                        self.DecodeCollision(defender.Collision(self), tmpx, tmpy)
                elif not isinstance(defender, Ground.Ground) and isinstance(defender, Plant.Plant):
                    self._world.AddToLogs(self.GetName() + " zjada " + defender.GetName())
                    self.DecodeCollision(defender.Collision(self), tmpx, tmpy)
                else:
                    self.DecodeCollision(Collisions.Collisions.MOVE, tmpx, tmpy)
                break

    def IsSameSpecies(self, defender):
        if isinstance(defender, Fox):
            return True
        else:
            return False

    def Color(self):
        return '#ff9900'
