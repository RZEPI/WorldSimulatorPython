from PySimpleGUI import PySimpleGUI as pg


class Gui:
    pg.theme("LightGrey1")

    def __init__(self, world, board=None):
        self.__world = world
        if board is None:
            board = [[] for _ in range(self.__world.GetHeight())]
        for y in range(0, self.__world.GetHeight()):
            for x in range(0, self.__world.GetWidth()):
                board[y].append(pg.Text(" ", background_color=self.__world.board[x][y].Color(), size=[1, 1], pad=1))
        self.__layout = [
            [pg.Button('Nowa Tura'), pg.Button('Zapisz do pliku'), pg.Button('Wczytaj z pliku')],
            board,
            [pg.Text(self.__world.GetLogs())]
        ]

    def GetLayout(self):
        return self.__layout
