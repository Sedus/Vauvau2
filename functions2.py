import os
from termcolor import cprint
from art import tprint
import random

import variables2
from character import *
from enemy import *

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

def clear():
    os.system("cls")

def start():
    tprint("vauvau    2", "tarty1")
    tprint("PRE-ALPHA    0.0.3", "tarty1")
    cprint("NYOMJ MEG BÁRMIT AZ INDULÁSHOZ!", "green", attrs=["bold"])
    input("> ")
    clear()

def rules():
    cprint("\nSzámok beírásával tudsz navigálni." + "\n" + "A számokhoz tartozó parancsot mellette írva találod.", "green", attrs=["bold"])

def heal(amount):
    Character.HP += amount
    variables2.loglist.insert(0, Character.name + " élete fel lett töltve " + str(Character.HP) + "-re!")

def usepotion():
    if Character.potion > 0:
        Character.potion -= 1
        if Character.HP + 30 > Character.HPMAX:
            heal(Character.HPMAX - Character.HP)
        else:
            heal(30)
    else:
        variables2.loglist.insert(0, "Nincs gyógyitalod!")

def useelixir():
    if Character.elixir > 0:
        Character.elixir -= 1
        heal(Character.HPMAX - Character.HP)
    else:
        variables2.loglist.insert(0, "Nincs elixíred!")

def createmap():
    for number5 in range(5):
        innerlist = []
        for number7 in range(7):
            #abc = listToString(random.choices(variables2.tiles))
            #abc = "bolt"
            abc = "erdő"
            innerlist.append(abc)
        variables2.map.append(innerlist)
    variables2.y_len = len(variables2.map)-1
    variables2.x_len = len(variables2.map[0])-1
    variables2.map2[variables2.y][variables2.x] = "X"

def print_map(map2):
    for i in map2:
        cprint('\n' + '+---' * 7 + '+', "red")
        for j in i:
            cprint('| ', "red", end='')
            cprint(format(j) + " ", "green", attrs=["bold"], end='')
        cprint('|', "red", end='')
    cprint('\n' + '+---' * 7 + '+', "red")

def tiledraw():
    icon = variables2.biom [variables2.map[variables2.y][variables2.x]] ["icon"]
    variables2.map2[variables2.y][variables2.x] = icon

def moveleft():
    tiledraw()
    variables2.x -= 1
    variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " balra lépett!")

def moveright():
    tiledraw()
    variables2.x += 1
    variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " jobbra lépett!")

def moveup():
    tiledraw()
    variables2.y -= 1
    variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " felfele lépett!")

def movedown():
    tiledraw()
    variables2.y += 1
    variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " lefele lépett!")

def weaponupgrade():
    if Character.gold >= 10:
        Character.attack += 2
        Character.gold -= 10
        variables2.loglist.insert(0, "Sikeresen fejlesztetted a fegyvered!")
    else:
        variables2.loglist.insert(0, "Nincs elég aranyad!")

def potbuy():
    if Character.gold >= 5:
        Character.potion += 1
        Character.gold -= 5
        variables2.loglist.insert(0, "Vettél egy gyógyitalt!")
    else:
        variables2.loglist.insert(0, "Nincs elég aranyad!")

def elixbuy():
    if Character.gold >= 20:
        Character.elixir += 1
        Character.gold -= 20
        variables2.loglist.insert(0, "Vettél egy elixírt!")
    else:
        variables2.loglist.insert(0, "Nincs elég aranyad!")

def equipmentlayout():
    clear()
    cprint("1 - FEGYVER", "green", attrs=["bold"])
    cprint("2 - VÉRT", "green", attrs=["bold"])
    cprint("3 - SISAK", "green", attrs=["bold"])
    cprint("4 - CIPŐ", "green", attrs=["bold"])
    cprint("5 - TALIZMÁN", "green", attrs=["bold"])