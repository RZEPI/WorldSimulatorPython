import random

import Organism
import Collisions
import defines


class Plant(Organism.Organism):
    def __init__(self, world, x, y, strength, initiative, name):
        super().__init__(world, x, y, strength, initiative, name)

    def Action(self):
        randNum = random.randint(0, defines.CHANCE_FOR_PLANT_TO_REPLICATE)
        if randNum == 1:
            self.Replicate(self.GetPosX(), self.GetPosY())

    def Collision(self, attacker):
        self.Die()
        return Collisions.Collisions.MOVE

