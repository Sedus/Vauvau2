import os
import sys
from termcolor import cprint
import time
from art import tprint
import random

import variables2
from character import *
from enemy import *

def draw():
    cprint("==============================================================================", "red")

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

def effect(text, color, delay):
    for char in text:
        cprint(char, color, end = "")
        sys.stdout.flush()
        time.sleep(delay)

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

def logprint():
    draw()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    draw()
    cprint("LEGUTÓBBI ESEMÉNYEK:", "green", attrs=["bold"])
    for result in variables2.loglist:
        cprint("    " + str(result), "magenta", attrs=["bold"])

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
            abc = "bolt"
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
    variables2.loglist.insert(0, Character.name + " balra lépett!\n")

def moveright():
    tiledraw()
    variables2.x += 1
    variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " jobbra lépett!\n")

def moveup():
    tiledraw()
    variables2.y -= 1
    variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " felfele lépett!\n")

def movedown():
    tiledraw()
    variables2.y += 1
    variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor
    variables2.loglist.insert(0, Character.name + " lefele lépett!\n")

def weaponupgrade():
    if Character.gold >= 10:
        Character.attack += 2
        Character.gold -= 10
        variables2.loglist.insert(0, "Sikeresen fejlesztetted a fegyvered!\n")
    else:
        variables2.loglist.insert(0, "Nincs elég aranyad!\n")

def potbuy():
    if Character.gold >= 5:
        Character.potion += 1
        Character.gold -= 5
        variables2.loglist.insert(0, "Vettél egy gyógyitalt!\n")
    else:
        variables2.loglist.insert(0, "Nincs elég aranyad!\n")

def elixbuy():
    if Character.gold >= 20:
        Character.elixir += 1
        Character.gold -= 20
        variables2.loglist.insert(0, "Vettél egy elixírt!\n")
    else:
        variables2.loglist.insert(0, "Nincs elég aranyad!\n")

def attack():
    if variables2.enemy_hp <= Character.attack:
        loot()
    else:
        variables2.enemy_hp -= Character.attack
        Character.HP -= variables2.enemy_atk
        variables2.loglist.insert(0, Character.name + " " + str(Character.attack) + " sebzést okozott " + variables2.mobs [variables2.enemy] ["name"] + "-nak.\n")
        variables2.loglist.insert(0, variables2.mobs [variables2.enemy] ["name"] + " " + str(variables2.enemy_atk) + " sebzést okozott " + Character.name + "-nak.")
        if variables2.player_hp <= 0:
            clear()
            cprint (variables2.mobs [variables2.enemy] ["name"] + " legyőzte " + Character.name + "...", "red")
            cprint("VÉGE", "red")
            input("> ")
            quit()

def loot():
    variables2.loglist.clear()
    variables2.loglist.insert(0, Character.name + " legyőzte " + (variables2.mobs [variables2.enemy] ["name"] + "-ot!"))
    variables2.loglist.insert(0, "Találtál " + str(variables2.mobs [variables2.enemy] ["gold"]) + " aranyat!\n")
    Character.gold += variables2.mobs [variables2.enemy] ["gold"]

def equipmentlayout():
    clear()
    draw()
    cprint("1 - FEGYVER", "green", attrs=["bold"])
    cprint("2 - VÉRT", "green", attrs=["bold"])
    cprint("3 - SISAK", "green", attrs=["bold"])
    cprint("4 - CIPŐ", "green", attrs=["bold"])
    cprint("5 - TALIZMÁN", "green", attrs=["bold"])
    draw()