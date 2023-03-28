import Organism


class Ground(Organism.Organism):
    def __init__(self, world, x, y):
        self._world = world
        self.__x = x
        self.__y = y

    def Color(self):
        return '#d9d9d9'
