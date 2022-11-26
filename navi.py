import variables2
from ui import *
from map import *

def moveleft():
    UI.tiledraw()
    Character.pos_x -= 1
    Map.map2[Character.pos_y][Character.pos_x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " balra lépett!")

def moveright():
    UI.tiledraw()
    Character.pos_x += 1
    Map.map2[Character.pos_y][Character.pos_x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " jobbra lépett!")

def moveup():
    UI.tiledraw()
    Character.pos_y -= 1
    Map.map2[Character.pos_y][Character.pos_x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " felfele lépett!")

def movedown():
    UI.tiledraw()
    Character.pos_y += 1
    Map.map2[Character.pos_y][Character.pos_x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " lefele lépett!")