import os
import sys
from termcolor import cprint
import time
from art import tprint
import random

import variables2

def draw():
    print ("==============================================================================")

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

def toplay():
    variables2.shop = False
    variables2.menu = False
    variables2.battle = False
    variables2.play = True
    variables2.battle = False

def start():
    tprint("vauvau    2", "tarty1")
    tprint("PRE-ALPHA    0.0.1", "tarty1")
    print("NYOMJ MEG BÁRMIT AZ INDULÁSHOZ!")
    input("> ")

def rules():
    print("Számok beírásával tudsz navigálni." + "\n" + "A számokhoz tartozó parancsot mellette írva találod.")
    input("> ")

def menu_layout():
    clear()

    effect("1 - ÚJ JÁTÉK\n", "green", 0.01)
    effect("2 - JÁTÉK BETÖLTÉSE\n", "blue", 0.01)
    effect("3 - SZABÁLYOK\n", "magenta", 0.01)
    effect("4 - KILÉPÉS\n", "yellow", 0.01)

    draw()

def menu_layout2():
    print("JELENLEGI POZÍCIÓ: " + variables2.biom[variables2.map[variables2.y][variables2.x]]["name"])
    draw()
    effect("NÉV: " + variables2.name + "\n", "blue", 0.01)
    effect("ÉLET:" + "|♥♥♥♥♥♥♥♥♥♥|" + str(variables2.player_hp) + "/" + str(variables2.player_hpmax) + "\n", "green", 0.01)
    effect("SEBZÉS:" + "|¤¤¤¤¤¤¤¤¤¤|" + str(variables2.player_atk) + "\n", "cyan", 0.01)
    effect("GYÓGYITAL: " + str(variables2.pot) + " darab\n", "red", 0.01)
    effect("ELIXÍR: " +str(variables2.elix) + " darab\n", "magenta", 0.01)
    effect("ARANY: " +str(variables2.gold) + "$\n", "yellow", 0.01)
    draw()
    effect("0 - MENTÉS ÉS KILÉPÉS\n", "green", 0.01)
    if variables2.y > 0:
        effect("1 - ▲ FEL\n", "green", 0.01)
    if variables2.x < variables2.x_len:
        effect("2 - ► JOBBRA\n", "green", 0.01)
    if variables2.y < variables2.y_len:
        effect("3 - ▼ LE\n", "green", 0.01)
    if variables2.x > 0:
        effect("4 - ◄ BALRA\n", "green", 0.01)
    if variables2.pot > 0:
        effect("5 - GYÓGYITAL HASZNÁLATA (30HP)\n", "green", 0.01)
    if variables2.elix > 0:
        effect("6 - ELIXÍR HASZNÁLATA (MAXHP)\n", "green", 0.01)
    if variables2.map[variables2.y][variables2.x] == "bolt":
        effect("7 - BELÉPÉS\n", "green", 0.01)
    draw()

def heal(amount):
    variables2.player_hp += amount
    print (variables2.name + " élete fel lett töltve " + str(variables2.player_hp) + "-re!")
    input("> ")

def usepotion():
    if variables2.pot > 0:
        variables2.pot -= 1
        if variables2.player_hp + 30 > variables2.player_hpmax:
            heal(variables2.player_hpmax - variables2.player_hp)
        else:
            heal(30)
    else:
        print("Nincs gyógyitalod!")
        input("> ")

def useelixir():
    if variables2.elix > 0:
        variables2.elix -= 1
        heal(variables2.player_hpmax - variables2.player_hp)
    else:
        print("Nincs elixíred!")
        input("> ")

def createmap():
    for number5 in range(5):
        innerlist = []
        for number7 in range(7):
            abc = listToString(random.choices(variables2.tiles))
            innerlist.append(abc)
        variables2.map.append(innerlist)
    variables2.y_len = len(variables2.map)-1
    variables2.x_len = len(variables2.map[0])-1
    variables2.map2[variables2.y][variables2.x] = "X"

def print_map(map2):
    clear()
    for i in map2:
        cprint('\n' + '+---' * 7 + '+')
        for j in i:
            cprint('| ', end='')
            cprint(format(j) + " ", "red", end='')
        cprint('|', end='')
    cprint('\n' + '+---' * 7 + '+')

def tiledraw():
    icon = variables2.biom [variables2.map[variables2.y][variables2.x]] ["icon"]
    variables2.map2[variables2.y][variables2.x] = icon

def moveleft():
    if variables2.x > 0:
        tiledraw()
        variables2.x -= 1
        variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor

def moveright():
    if variables2.x < variables2.x_len:
        tiledraw()
        variables2.x += 1
        variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor

def moveup():
    if variables2.y > 0:
        tiledraw()
        variables2.y -= 1
        variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor

def movedown():
    if variables2.y < variables2.y_len:
        tiledraw()
        variables2.y += 1
        variables2.map2[variables2.y][variables2.x] = "X" # kövi kurzor

def toshop():
    if variables2.map[variables2.y][variables2.x] == "bolt":
            variables2.menu = False
            variables2.play = False
            variables2.shop = True

def shoplayout():
    clear()
    draw()
    print("Üdvözöllek a boltban!")
    draw()
    cprint("SEBZÉS:" + "|¤¤¤¤¤¤¤¤¤¤|" + str(variables2.player_atk), "cyan")
    cprint("GYÓGYITAL: " + str(variables2.pot) + " darab", "red")
    cprint("ELIXÍR: " +str(variables2.elix) + " darab", "magenta")
    cprint("ARANY: " +str(variables2.gold) + "$", "yellow")

    draw()
    effect("1 - FEGYVER FEJLESZTÉSE (+2 SEBZÉS) - 10 ARANY\n", "cyan", 0.01)
    effect("2 - GYÓGYITAL VÁSÁRLÁSA (+30HP) - 5 ARANY\n", "red", 0.01)
    effect("3 - ELIXÍR VÁSÁRLÁSA (MAXHP) - 20 ARANY\n", "magenta", 0.01)
    effect("4 - KILÉPÉS\n", "yellow", 0.01)
    draw()

def weaponupgrade():
    if variables2.gold >= 10:
        variables2.player_atk += 2
        variables2.gold -= 10
        print ("Sikeresen fejlesztetted a fegyvered!")
    else:
        print ("Nincs elég aranyad!")
    input("> ")

def potbuy():
    if variables2.gold >= 5:
        variables2.pot += 1
        variables2.gold -= 5
        print ("Vettél egy gyógyitalt!")
    else:
        print ("Nincs elég aranyad!")
    input("> ")

def elixbuy():
    if variables2.gold >= 20:
        variables2.elix += 1
        variables2.gold -= 20
        print ("Vettél egy elixírt!")
    else:
        print ("Nincs elég aranyad!")
    input("> ")

def spawnenemychance():
    if variables2.biom [variables2.map[variables2.y][variables2.x]] ["spawn_enemy"]:
        if random.randint (1, 10) <= 100:
            variables2.play = False
            variables2.battle = True
            variables2.enemy = random.choice(variables2.enemy_list)
            variables2.mobs ["Goblin"] ["name"] = random.choice(variables2.goblin_names)
            variables2.mobs ["Ork"] ["name"] = random.choice(variables2.ork_names)
            variables2.mobs ["Slime"] ["name"] = random.choice(variables2.slime_names)
            variables2.enemy_hp = variables2.mobs [variables2.enemy] ["hp"]
            variables2.enemy_atk = variables2.mobs [variables2.enemy] ["atk"]

def battlelayout():
    clear()
    draw()
    print("Győzd le " + variables2.mobs [variables2.enemy] ["name"] + "-ot!")
    draw()
    print(variables2.mobs [variables2.enemy] ["name"] + " élete: " + str(variables2.enemy_hp))
    print(variables2.name + " élete: " + str(variables2.player_hp) + "/" + str(variables2.player_hpmax))
    draw()
    print("GYÓGYITAL: " + str(variables2.pot) + " darab")
    print("ELIXÍR: " +str(variables2.elix) + " darab")
    draw()
    print("1 - TÁMADÁS")
    print("2 - GYÓGYITAL HASZNÁLATA (30HP)")
    print("3 - ELIXÍR HASZNÁLATA (MAXHP)")
    draw()

def attack():
    variables2.enemy_hp -= variables2.player_atk
    variables2.player_hp -= variables2.enemy_atk
    print (variables2.name + " " + str(variables2.player_atk) + " sebzést okozott " + variables2.mobs [variables2.enemy] ["name"] + "-nak.")
    print (variables2.mobs [variables2.enemy] ["name"] + " " + str(variables2.enemy_atk) + " sebzést okozott " + variables2.name + "-nak.")
    input("> ")
    if variables2.enemy_hp <= 0:
        loot()
    if variables2.player_hp <= 0:
        clear()
        print (variables2.mobs [variables2.enemy] ["name"] + " legyőzte " + variables2.name + "...")
        print("VÉGE")
        input("> ")
        quit()

def loot():
    clear()
    print (variables2.name + " legyőzte " + (variables2.mobs [variables2.enemy] ["name"] + "-ot!"))
    print ("Találtál " + str(variables2.mobs [variables2.enemy] ["gold"]) + " aranyat!")
    input("> ")
    toplay()
