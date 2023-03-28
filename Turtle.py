import random

import Animal
import Collisions
import Ground
import Plant
import defines


class Turtle(Animal.Animal):
    def __init__(self, world, x, y, strength=defines.WOLF_STRENGTH):
        super().__init__(world, x, y, strength, initiative=defines.WOLF_INIT, name=defines.WOLF_NAME)

    def Replicate(self, posOfParentX, posOfParentY):
        newOrgPosX, newOrgPosY = self.SearchForFreePos(posOfParentX, posOfParentY)
        if newOrgPosX > -1 and self.GetAge() > 5 and self._world.board[posOfParentX][posOfParentY].GetAge() > 5:
            self.SetAge(0)
            self._world.board[posOfParentX][posOfParentY].SetAge(0)
            newOrg = Turtle(self._world, newOrgPosX, newOrgPosY)
            self._world.AddOrg(newOrg)
            self._world.board[newOrgPosX][newOrgPosY] = newOrg
            self._world.AddToLogs(self.GetName() + " rozmnozyl sie")

    def IsSameSpecies(self, defender):
        if isinstance(defender, Turtle):
            return True
        else:
            return False

    def Collision(self, attacker):
        if attacker.GetStrength() > defines.STRENGTH_TO_KILL_TURTLE:
            self.Die()
            return Collisions.Collisions.MOVE
        else:
            return Collisions.Collisions.TURTLE_COUNTER

    def Action(self):
        move = random.randint(0, 3)
        if move == 0:
            while True:
                tmpx, tmpy = self.RandomisePos(self.GetPosX(), self.GetPosY())
                if self._world.CheckIfIsBounds(tmpx, tmpy):
                    defender = self._world.board[tmpx][tmpy]
                    if self.IsSameSpecies(defender):
                        self.Replicate(defender.GetPosX(), defender.GetPosY())
                        self._world.AddToLogs(self.GetName() + " rozmnozyl sie")
                    elif not isinstance(defender, Ground.Ground) and isinstance(defender, Animal.Animal):
                        self._world.AddToLogs(self.GetName() + " atakuje " + defender.GetName())
                        self.DecodeCollision(defender.Collision(self), tmpx, tmpy)
                    elif not isinstance(defender, Ground.Ground) and isinstance(defender, Plant.Plant):
                        self._world.AddToLogs(self.GetName() + " zjada " + defender.GetName())
                        self.DecodeCollision(defender.Collision(self), tmpx, tmpy)
                    else:
                        self.DecodeCollision(Collisions.Collisions.MOVE, tmpx, tmpy)
                    break

    def Color(self):
        return '#006600'
