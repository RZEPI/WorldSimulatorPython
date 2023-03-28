import Animal
import defines


class Wolf(Animal.Animal):
    def __init__(self, world, x, y, strength=defines.WOLF_STRENGTH):
        super().__init__(world, x, y, strength, initiative=defines.WOLF_INIT, name=defines.WOLF_NAME)

    def Replicate(self, posOfParentX, posOfParentY):
        newOrgPosX, newOrgPosY = self.SearchForFreePos(posOfParentX, posOfParentY)
        if newOrgPosX > -1 and self.GetAge() > 5 and self._world.board[posOfParentX][posOfParentY].GetAge() > 5:
            self.SetAge(0)
            self._world.board[posOfParentX][posOfParentY].SetAge(0)
            newOrg = Wolf(self._world, newOrgPosX, newOrgPosY, defines.WOLF_STRENGTH)
            self._world.AddOrg(newOrg)
            self._world.board[newOrgPosX][newOrgPosY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozmnozyl sie")

    def IsSameSpecies(self, defender):
        if isinstance(defender, Wolf):
            return True
        else:
            return False

    def Color(self):
        return '#ff66ff'