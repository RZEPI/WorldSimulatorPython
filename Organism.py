import Direction
import World

import random
import Collisions
import defines


class Organism:
    def __init__(self, world, x, y, strength, initiative, name):
        self._world = world
        self.__x = x
        self.__y = y
        self.__initiative = initiative
        self.__strength = strength
        self.__alive = True
        self.__name = name
        self.__age = 0

    @staticmethod
    def RandomisePos(prevx, prevy):
        option = random.randint(0, 3)
        match option:
            case Direction.Direction.UP.value:
                prevy -= 1
            case Direction.Direction.DOWN.value:
                prevy += 1
            case Direction.Direction.RIGHT.value:
                prevx += 1
            case Direction.Direction.LEFT.value:
                prevx -= 1
        return prevx, prevy

    def SearchForFreePos(self, posx, posy):
        import Ground
        i = 4
        while i != 0:
            tmpx, tmpy = self.RandomisePos(posx, posy)
            i -= 1
            if self._world.CheckIfIsBounds(tmpx, tmpy):

                if isinstance(self._world.board[tmpx][tmpy], Ground.Ground):
                    return tmpx, tmpy
        return -1, -1

    def Die(self):
        self._world.AddToLogs(self.GetName() + " umiera")
        self.__alive = False

    def IsAlive(self):
        return self.__alive

    def GetName(self):
        return self.__name

    def GetPosX(self):
        return self.__x

    def GetPosY(self):
        return self.__y

    def SetPosX(self, x):
        self.__x = x

    def SetPosY(self, y):
        self.__y = y

    def GetStrength(self):
        return self.__strength

    def GetInit(self):
        return self.__initiative

    def SetStrength(self, strength):
        self.__strength = strength

    def SetAge(self, age):
        self.__age = age

    def GetAge(self):
        return self.__age

    def GetSign(self):
        match self.__name:
            case defines.HUMAN_NAME:
                return defines.HUMAN_SIGN
            case defines.FOX_NAME:
                return defines.FOX_SIGN
            case defines.MILT_NAME:
                return defines.MILT_SIGN
            case defines.SOSHOGWEED_NAME:
                return defines.SOSHOGWEED_SIGN
            case defines.GUARANA_NAME:
                return defines.GUARANA_SIGN
            case defines.SHEEP_NAME:
                return defines.SHEEP_SIGN
            case defines.TURTLE_NAME:
                return defines.TURTLE_SIGN
            case defines.BELLADONNA_NAME:
                return defines.BELLADONNA_SIGN
            case defines.MECHSHEEP_NAME:
                return defines.MECHSHEEP_SIGN
            case defines.GRASS_NAME:
                return defines.GUARANA_SIGN
            case defines.WOLF_NAME:
                return defines.WOLF_SIGN

    def DecodeCollision(self, collision, tmpx, tmpy):
        import Ground
        match collision:
            case Collisions.Collisions.MOVE:
                self._world.board[self.GetPosX()][self.GetPosY()] = Ground.Ground(self._world, self.GetPosX(), self.GetPosY())
                self.SetPosX(tmpx)
                self.SetPosY(tmpy)
                self._world.board[tmpx][tmpy] = self
            case Collisions.Collisions.DIE:
                self._world.AddToLogs(self.GetName() + " umiera")
                self.Die()
            case Collisions.Collisions.HUMAN_ALZARUS_SHIELD:
                self._world.AddToLogs(self.GetName() + " zostal odbity przez tarcze Alzura")
                self.SearchForFreePos(tmpx, tmpy)
            case Collisions.Collisions.TURTLE_COUNTER:
                self._world.AddToLogs(self.GetName() + " zostal odbity przez zlowia")
            case Collisions.Collisions.GUARANA_BOOST:
                self._world.board[self.GetPosX()][self.GetPosY()] = Ground.Ground(self._world, self.GetPosX(), self.GetPosY())
                self.SetPosX(tmpx)
                self.SetPosY(tmpy)
                self._world.board[tmpx][tmpy] = self
                self.SetStrength(self.GetStrength()+defines.GUARANA_BOOST_VAL)
                self._world.AddToLogs(self.GetName() + " zdjadl guarane i otrzymuje +3 do sily")


