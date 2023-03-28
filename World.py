import Belladona
import Direction
import Fox
import Grass
import Guarana
import Gui
import Ground
import MechSheep
import Milt
import Sheep
import SosHogweed
import Turtle
import Wolf
import defines
from PySimpleGUI import PySimpleGUI as pg


class World:
    #organisms = []

    # orgToAdd = []
    # orgToDel = []

    def __init__(self, nameOfFile):
        self.__height = defines.DEFAULT_Y
        self.__width = defines.DEFAULT_X
        self.__h = None
        self.board = [[] for _ in range(self.__height)]
        self.__logs = "wygenerowano swiat\n"
        self.organisms = []
        self.window = pg.Window("Symlator swiata", layout=[[pg.Button("Start")]])
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                self.board[i].append(Ground.Ground(self, i, j))
        self.GenerateOrgListFromFile(nameOfFile)

    def GetWidth(self):
        return self.__width

    def GetHeight(self):
        return self.__height

    def GenerateOrgListFromFile(self, nameOfFile):
        f = open(nameOfFile, "r")
        lines = f.readlines()
        for i in lines:
            self.DecodeOrg(i)

    def AddOrg(self, organism):
        inserted = False
        self.board[organism.GetPosX()][organism.GetPosY()] = organism
        for o in self.organisms:
            if organism.GetInit() > o.GetInit():
                self.organisms.insert(self.organisms.index(o), organism)
                inserted = True
                break
        if not inserted:
            self.organisms.append(organism)

    def AddToLogs(self, mess):
        self.__logs += mess + '\n'

    def GetLogs(self):
        return self.__logs

    def ClearLogs(self):
        self.__logs = ""

    def CheckIfIsBounds(self, x, y):
        if 0 <= x < self.__width and 0 <= y < self.__height:
            return True
        else:
            return False

    # file:
    # type posX posY strength (for human duration of ability and cooldown)

    def DecodeOrg(self, line):
        import Human
        info = line.split()
        match info[0]:
            case defines.HUMAN_SIGN:
                self.__h = Human.Human(self, int(info[1]), int(info[2]), int(info[3]), int(info[4]), int(info[5]))
                if int(info[4]) != defines.DURATION_OF_ABILITY and int(info[4]) != 0:
                    self.__h.ActiveAbility()
                self.AddOrg(self.__h)
            case defines.MECHSHEEP_SIGN:
                if len(info) > 3:
                    newOrg = MechSheep.MechSheep(self, int(info[1]), int(info[2]), int(info[3]))
                else:
                    newOrg = MechSheep.MechSheep(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)
            case defines.SHEEP_SIGN:
                if len(info) > 3:
                    newOrg = Sheep.Sheep(self, int(info[1]), int(info[2]), int(info[3]))
                else:
                    newOrg = Sheep.Sheep(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)
            case defines.WOLF_SIGN:
                if len(info) > 3:
                    newOrg = Wolf.Wolf(self, int(info[1]), int(info[2]), int(info[3]))
                else:
                    newOrg = Wolf.Wolf(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)
            case defines.TURTLE_SIGN:
                if len(info) > 3:
                    newOrg = Turtle.Turtle(self, int(info[1]), int(info[2]), int(info[3]))
                else:
                    newOrg = Turtle.Turtle(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)
            case defines.FOX_SIGN:
                if len(info) > 3:
                    newOrg = Fox.Fox(self, int(info[1]), int(info[2]), int(info[3]))
                else:
                    newOrg = Fox.Fox(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)
            case defines.GUARANA_SIGN:
                newOrg = Guarana.Guarana(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)
            case defines.BELLADONNA_SIGN:
                newOrg = Belladona.Belladona(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)
            case defines.SOSHOGWEED_SIGN:
                newOrg = SosHogweed.SosHogweed(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)
            case defines.GRASS_SIGN:
                newOrg = Grass.Grass(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)
            case defines.MILT_SIGN:
                newOrg = Milt.Milt(self, int(info[1]), int(info[2]))
                self.AddOrg(newOrg)

    def SetDirectionForHuman(self, event):
        match event:
            case "Up:38":
                self.__h.SetDirection(Direction.Direction.UP)
            case "Down:40":
                self.__h.SetDirection(Direction.Direction.DOWN)
            case "Left:37":
                self.__h.SetDirection(Direction.Direction.LEFT)
            case "Right:39":
                self.__h.SetDirection(Direction.Direction.RIGHT)

    def ExecuteTurn(self):
        for o in self.organisms:
            if o.IsAlive():
                o.Action()
                o.SetAge(o.GetAge() + 1)

        for o in self.organisms:
            if not o.IsAlive():
                self.organisms.pop(self.organisms.index(o))

        self.window.close()
        gui = Gui.Gui(self)
        self.window = pg.Window("Symulator siwata", gui.GetLayout(), finalize=True, return_keyboard_events=True)
        self.ClearLogs()

    def SaveToFile(self):
        import Human
        toFile = ""
        for o in self.organisms:
            toFile += str(o.GetSign()) + " " + str(o.GetPosX()) + " " + str(o.GetPosY()) + " " + str(o.GetStrength())
            if isinstance(o, Human.Human):
                toFile += " " + str(o.GetDurationOfAbility()) + " " + str(o.GetCooldownOfAbility())
            toFile += " \n"
        file = open("savedFile.txt", "w")
        file.write(toFile)
        file.close()

    def GameOver(self):
        if self.__h is None:
            return False
        else:
            return not self.__h.IsAlive()

    def ActiveHumanAbility(self):
        self.__h.ActiveAbility()
