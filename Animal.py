import Organism
import Collisions
import Ground
import Plant


class Animal(Organism.Organism):

    def __init__(self, world, x, y, strength, initiative, name):
        super().__init__(world, x, y, strength, initiative, name)

    def Action(self):
        while True:
            tmpx, tmpy = self.RandomisePos(self.GetPosX(), self.GetPosY())
            if self._world.CheckIfIsBounds(tmpx, tmpy):
                defender = self._world.board[tmpx][tmpy]
                if self.IsSameSpecies(defender):
                    self.Replicate(defender.GetPosX(), defender.GetPosY())
                    self._world.AddToLogs(self.GetName() + " rozmnozyl sie")
                elif not isinstance(defender, Ground.Ground) and isinstance(defender, Animal):
                    self._world.AddToLogs(self.GetName() + " atakuje " + defender.GetName())
                    self.DecodeCollision(defender.Collision(self), tmpx, tmpy)
                elif not isinstance(defender, Ground.Ground) and isinstance(defender, Plant.Plant):
                    self._world.AddToLogs(self.GetName() + " zjada " + defender.GetName())
                    self.DecodeCollision(defender.Collision(self), tmpx, tmpy)
                else:
                    self.DecodeCollision(Collisions.Collisions.MOVE, tmpx, tmpy)
                break

    def Collision(self, attacker):
        if attacker.GetStrength() < self.GetStrength():
            return Collisions.Collisions.DIE
        else:
            self.Die()
            return Collisions.Collisions.MOVE

