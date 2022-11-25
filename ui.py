import os
import variables2
from functions2 import print_map,draw,logprint
from termcolor import cprint
from character import *

state = "menu"
counter = 0
menu = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]
menu2 = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]
play = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]
play2 = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]

def switchstate(hova):
    global state
    if hova == "menu":
        counter = 0
        state = hova
        os.system("cls")
        menu_layout()
        menu[counter] = ">" + menu[counter] + "<"
        navmenuprint(menu)
    if hova == "play":
        counter = 0
        state = hova
        os.system("cls")
        print_map(variables2.map2)
        menu_layout2()
        play[counter] = ">" + play[counter] + "<"
        navmenuprint(play)

def navup(list1, list2):
    global counter
    if counter != 0:
        list1[counter] = list2[counter]
        counter -= 1
        list1[counter] = "> " + list1[counter] + " <"
    else:
        list1[counter] = list2[counter]
        counter -= 1
        list1[counter] = "> " + list1[counter] + " <"
        counter = len(list1) - 1

def navdown(list1,list2):
    global counter
    if counter != len(list1) - 1:
        list1[counter] = list2[counter]
        counter += 1
        list1[counter] = "> " + list1[counter] + " <"
    else:
        list1[counter] = list2[counter]
        counter = 0
        list1[counter] = "> " + list1[counter] + " <"

def menu_layout():
    cprint("1 - ÚJ JÁTÉK", "green", attrs=["bold"])
    cprint("2 - JÁTÉK BETÖLTÉSE", "green", attrs=["bold"])
    cprint("3 - SZABÁLYOK", "green", attrs=["bold"])
    cprint("4 - KILÉPÉS", "green", attrs=["bold"])

def menu_layout2():
    draw()
    cprint("JELENLEGI POZÍCIÓ: " + variables2.biom[variables2.map[variables2.y][variables2.x]]["name"], "green", attrs=["bold"])
    draw()
    cprint("NÉV: " + Character.name, "green", attrs=["bold"])
    cprint("ÉLET: " + str(Character.get_HP(Character)) + "/" + str(variables2.player_hpmax), "green", attrs=["bold"])
    cprint("SEBZÉS: " + str(Character.get_attack(Character)), "green", attrs=["bold"])
    cprint("GYÓGYITAL: " + str(variables2.pot) + " darab", "green", attrs=["bold"])
    cprint("ELIXÍR: " + str(variables2.elix) + " darab", "green", attrs=["bold"])
    cprint("ARANY: " + str(variables2.gold) + "$", "green", attrs=["bold"])
    draw()

def navmenuprint(list):
    for i in list:
        if i == list[counter]:
            cprint (i, "white", "on_green", attrs=["bold"])
        else:
            cprint (i, "green", attrs=["bold"])
    logprint()
