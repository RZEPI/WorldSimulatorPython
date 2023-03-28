import Animal
import defines


class Sheep(Animal.Animal):
    def __init__(self, world, x, y, strength=defines.SHEEP_STRENGTH):
        super().__init__(world, x, y, strength, initiative=defines.SHEEP_INIT, name=defines.SHEEP_NAME)

    def Replicate(self, posOfParentX, posOfParentY):
        newOrgPosX, newOrgPosY = self.SearchForFreePos(posOfParentX, posOfParentY)
        if newOrgPosX > -1 and self.GetAge() > 5 and self._world.board[posOfParentX][posOfParentY].GetAge() > 5:
            self.SetAge(0)
            self._world.board[posOfParentX][posOfParentY].SetAge(0)
            newOrg = Sheep(self._world, newOrgPosX, newOrgPosY)
            self._world.AddOrg(newOrg)
            self._world.board[newOrgPosX][newOrgPosY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozmnozyl sie")

    def IsSameSpecies(self, defender):
        if isinstance(defender, Sheep):
            return True
        else:
            return False

    def Color(self):
        return '#8c8c8c'
