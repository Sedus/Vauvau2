import os
import sys
from termcolor import cprint
import time
from art import tprint
import random

import variables2

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

def toplay():
    variables2.shop = False
    variables2.menu = False
    variables2.battle = False
    variables2.play = True
    variables2.battle = False

def start():
    tprint("vauvau    2", "tarty1")
    tprint("PRE-ALPHA    0.0.2", "tarty1")
    cprint("NYOMJ MEG BÁRMIT AZ INDULÁSHOZ!", "green")
    input("> ")

def rules():
    cprint("Számok beírásával tudsz navigálni." + "\n" + "A számokhoz tartozó parancsot mellette írva találod.")
    input("> ")

def menu_layout():
    clear()

    cprint("1 - ÚJ JÁTÉK", "green")
    cprint("2 - JÁTÉK BETÖLTÉSE", "blue")
    cprint("3 - SZABÁLYOK", "magenta")
    cprint("4 - KILÉPÉS", "yellow")

    draw()

def menu_layout2():
    cprint("JELENLEGI POZÍCIÓ: " + variables2.biom[variables2.map[variables2.y][variables2.x]]["name"], "magenta")
    draw()
    cprint("NÉV: " + variables2.name, "blue")
    cprint("ÉLET:" + "|♥♥♥♥♥♥♥♥♥♥|" + str(variables2.player_hp) + "/" + str(variables2.player_hpmax), "green")
    cprint("SEBZÉS:" + "|¤¤¤¤¤¤¤¤¤¤|" + str(variables2.player_atk), "cyan")
    cprint("GYÓGYITAL: " + str(variables2.pot) + " darab", "red")
    cprint("ELIXÍR: " + str(variables2.elix) + " darab", "magenta")
    cprint("ARANY: " + str(variables2.gold) + "$", "yellow")
    draw()
    
    cprint("0 - MENTÉS ÉS KILÉPÉS", "green")
    if variables2.y > 0:
        cprint("1 - ▲ FEL", "green")
    if variables2.x < variables2.x_len:
        cprint("2 - ► JOBBRA", "green")
    if variables2.y < variables2.y_len:
        cprint("3 - ▼ LE", "green")
    if variables2.x > 0:
        cprint("4 - ◄ BALRA", "green")
    if variables2.pot > 0:
        cprint("5 - GYÓGYITAL HASZNÁLATA (30HP)", "green")
    if variables2.elix > 0:
        cprint("6 - ELIXÍR HASZNÁLATA (MAXHP)", "green")
    if variables2.map[variables2.y][variables2.x] == "bolt":
        cprint("7 - BELÉPÉS", "green")
    draw()

def heal(amount):
    variables2.player_hp += amount
    cprint (variables2.name + " élete fel lett töltve " + str(variables2.player_hp) + "-re!", "green")
    input("> ")

def usepotion():
    if variables2.pot > 0:
        variables2.pot -= 1
        if variables2.player_hp + 30 > variables2.player_hpmax:
            heal(variables2.player_hpmax - variables2.player_hp)
        else:
            heal(30)
    else:
        cprint("Nincs gyógyitalod!", "green")
        input("> ")

def useelixir():
    if variables2.elix > 0:
        variables2.elix -= 1
        heal(variables2.player_hpmax - variables2.player_hp)
    else:
        cprint("Nincs elixíred!", "green")
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
    cprint("Üdvözöllek a boltban!")
    draw()
    cprint("SEBZÉS:" + "|¤¤¤¤¤¤¤¤¤¤|" + str(variables2.player_atk), "cyan")
    cprint("GYÓGYITAL: " + str(variables2.pot) + " darab", "red")
    cprint("ELIXÍR: " +str(variables2.elix) + " darab", "magenta")
    cprint("ARANY: " +str(variables2.gold) + "$", "yellow")

    draw()
    cprint("1 - FEGYVER FEJLESZTÉSE (+2 SEBZÉS) - 10 ARANY", "cyan")
    cprint("2 - GYÓGYITAL VÁSÁRLÁSA (+30HP) - 5 ARANY", "red")
    cprint("3 - ELIXÍR VÁSÁRLÁSA (MAXHP) - 20 ARANY", "magenta")
    cprint("4 - KILÉPÉS", "yellow")
    draw()

def weaponupgrade():
    if variables2.gold >= 10:
        variables2.player_atk += 2
        variables2.gold -= 10
        cprint ("Sikeresen fejlesztetted a fegyvered!", "green")
    else:
        cprint ("Nincs elég aranyad!", "green")
    input("> ")

def potbuy():
    if variables2.gold >= 5:
        variables2.pot += 1
        variables2.gold -= 5
        cprint ("Vettél egy gyógyitalt!", "green")
    else:
        cprint ("Nincs elég aranyad!", "green")
    input("> ")

def elixbuy():
    if variables2.gold >= 20:
        variables2.elix += 1
        variables2.gold -= 20
        cprint ("Vettél egy elixírt!", "green")
    else:
        cprint ("Nincs elég aranyad!", "green")
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
    cprint("Győzd le " + variables2.mobs [variables2.enemy] ["name"] + "-ot!", "green")
    draw()
    cprint(variables2.mobs [variables2.enemy] ["name"] + " élete: " + str(variables2.enemy_hp), "green")
    cprint(variables2.name + " élete: " + str(variables2.player_hp) + "/" + str(variables2.player_hpmax), "green")
    draw()
    cprint("GYÓGYITAL: " + str(variables2.pot) + " darab", "green")
    cprint("ELIXÍR: " +str(variables2.elix) + " darab", "green")
    draw()
    cprint("1 - TÁMADÁS", "green")
    cprint("2 - GYÓGYITAL HASZNÁLATA (30HP)", "green")
    cprint("3 - ELIXÍR HASZNÁLATA (MAXHP)", "green")
    draw()

def attack():
    variables2.enemy_hp -= variables2.player_atk
    variables2.player_hp -= variables2.enemy_atk
    cprint (variables2.name + " " + str(variables2.player_atk) + " sebzést okozott " + variables2.mobs [variables2.enemy] ["name"] + "-nak.", "green")
    cprint (variables2.mobs [variables2.enemy] ["name"] + " " + str(variables2.enemy_atk) + " sebzést okozott " + variables2.name + "-nak.", "green")
    input("> ")
    if variables2.player_hp <= 0:
        clear()
        cprint (variables2.mobs [variables2.enemy] ["name"] + " legyőzte " + variables2.name + "...", "red")
        cprint("VÉGE", "red")
        input("> ")
        quit()
    if variables2.enemy_hp <= 0:
        loot()

def loot():
    clear()
    cprint (variables2.name + " legyőzte " + (variables2.mobs [variables2.enemy] ["name"] + "-ot!"), "green")
    cprint ("Találtál " + str(variables2.mobs [variables2.enemy] ["gold"]) + " aranyat!", "green")
    input("> ")
    toplay()
