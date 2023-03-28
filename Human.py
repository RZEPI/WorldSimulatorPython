import Animal
import Direction
import Plant
import defines
import Collisions
import Ground


class Human(Animal.Animal):
    def __init__(self, world, x, y, strength=defines.HUMAN_STRENGTH, durationOfAbility=defines.DURATION_OF_ABILITY, cooldownOfAbility=defines.COOLDOWN_OF_ABILITY ):
        super().__init__(world, x, y, strength, initiative=defines.HUMAN_INIT, name=defines.HUMAN_NAME)
        self.__moveDirection = None
        self.__abilityOn = False
        self.__durationOfAbility = durationOfAbility
        self.__cooldownOfAbility = cooldownOfAbility

    def SetDirection(self, direction):
        match direction:
            case Direction.Direction.UP:
                print("up")
                self.__moveDirection = Direction.Direction.UP
            case Direction.Direction.DOWN:
                print("down")
                self.__moveDirection = Direction.Direction.DOWN
            case Direction.Direction.LEFT:
                print("left")
                self.__moveDirection = Direction.Direction.LEFT
            case Direction.Direction.RIGHT:
                print("right")
                self.__moveDirection = Direction.Direction.RIGHT

    def GetDurationOfAbility(self):
        return self.__durationOfAbility

    def GetCooldownOfAbility(self):
        return self.__cooldownOfAbility

    def IsAbilityOn(self):
        return self.__abilityOn

    def MoveInDirection(self):
        tmpPosX = self.GetPosX()
        tmpPosY = self.GetPosY()
        match self.__moveDirection:
            case Direction.Direction.UP:
                tmpPosY -= 1
            case Direction.Direction.DOWN:
                tmpPosY += 1
            case Direction.Direction.LEFT:
                tmpPosX -= 1
            case Direction.Direction.RIGHT:
                tmpPosX += 1
            case _:
                return
        if self._world.CheckIfIsBounds(tmpPosX, tmpPosY):
            defender = self._world.board[tmpPosX][tmpPosY]
            if isinstance(defender, Animal.Animal):
                self._world.AddToLogs(self.GetName() + " atakuje " + defender.GetName())
                self.DecodeCollision(defender.Collision(self), tmpPosX, tmpPosY)
            elif isinstance(defender, Plant.Plant):
                self._world.AddToLogs(self.GetName() + " zjada " + defender.GetName())
                self.DecodeCollision(defender.Collision(self), tmpPosX, tmpPosY)
            else:
                self.DecodeCollision(Collisions.Collisions.MOVE, tmpPosX, tmpPosY)

    def ActiveAbility(self):
        if self.__cooldownOfAbility == 0 and not self.IsAbilityOn():
            self._world.AddToLogs("specjalna umiejetnosc czlowieka zostala aktywowana")
            self.__abilityOn = True

    def CheckAbility(self):
        if self.IsAbilityOn():
            if self.__durationOfAbility != 0:
                self.__durationOfAbility -= 1
            else:
                self._world.AddToLogs("specjalna umiejetnosc czlowieka skonczyla sie")
                self.__abilityOn = False
                self.__cooldownOfAbility = defines.COOLDOWN_OF_ABILITY
        else:
            if self.__cooldownOfAbility != 0:
                self.__cooldownOfAbility -= 1
            else:
                self.__durationOfAbility = defines.DURATION_OF_ABILITY

    def Action(self):
        self.MoveInDirection()
        self.CheckAbility()

    def Collision(self, attacker):
        if self.IsAbilityOn():
            return Collisions.Collisions
        else:
            if attacker.GetStrength() < self.GetStrength():
                return Collisions.Collisions.DIE
            else:
                self.Die()
                return Collisions.Collisions.MOVE

    def Color(self):
        return '#000000'
