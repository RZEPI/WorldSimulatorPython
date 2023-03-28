import World
from PySimpleGUI import PySimpleGUI as pg


w = World.World("startOrg.txt")

w.ExecuteTurn()

while not w.GameOver():
    event, value = w.window.Read()
    if event == pg.WIN_CLOSED:
        break
    if event == 'q':
        w.ActiveHumanAbility()
    if event == 'Up:38' or event == 'Down:40' or event == 'Right:39' or event == 'Left:37':
        w.SetDirectionForHuman(event)
    if event == 'Nowa Tura':
        print("nowa tura")
        w.ExecuteTurn()
    if event == 'Zapisz do pliku':
        w.SaveToFile()
    if event == 'Wczytaj z pliku':
        w.window.close()
        w = World.World("savedFile.txt")
        w.ExecuteTurn()

    # print(event)


print("End of game")

