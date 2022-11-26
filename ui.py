import os
import variables2
from functions2 import print_map
from termcolor import cprint
from art import tprint
from character import *

class UI:
    state = None
    counter = 0
    menu = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]
    menu2 = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]
    play = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]
    play2 = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]
    shop = ["FEGYVER FEJLESZTÉSE (+2 SEBZÉS) - 10 ARANY", "GYÓGYITAL VÁSÁRLÁSA (+30HP) - 5 ARANY", "ELIXÍR VÁSÁRLÁSA (MAXHP) - 20 ARANY", "KILÉPÉS"]
    shop2 = ["FEGYVER FEJLESZTÉSE (+2 SEBZÉS) - 10 ARANY", "GYÓGYITAL VÁSÁRLÁSA (+30HP) - 5 ARANY", "ELIXÍR VÁSÁRLÁSA (MAXHP) - 20 ARANY", "KILÉPÉS"]
    battle = ["TÁMADÁS", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)"]
    battle2 = ["TÁMADÁS", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)"]

    def switchstate(hova):
        if hova == "menu":
            UI.counter = 0
            UI.state = hova
            UI.menu = UI.menu2.copy()
            os.system("cls")
            UI.menu[UI.counter] = "> " + UI.menu[UI.counter] + " <"
            UI.navmenuprint(UI.menu)
        if hova == "play":
            UI.counter = 0
            UI.state = hova
            UI.play = UI.play2.copy()
            os.system("cls")
            print_map(variables2.map2)
            UI.menu_layout2()
            UI.play[UI.counter] = "> " + UI.play[UI.counter] + " <"
            UI.navmenuprint(UI.play)
        if hova == "shop":
            UI.counter = 0
            UI.state = hova
            UI.shop = UI.shop2.copy()
            os.system("cls")
            UI.shoplayout()
            UI.shop[UI.counter] = "> " + UI.shop[UI.counter] + " <"
            UI.navmenuprint(UI.shop)
        if hova == "battle":
            UI.counter = 0
            UI.state = hova
            UI.battle = UI.battle2.copy()
            os.system("cls")
            UI.battlelayout()
            UI.battle[UI.counter] = "> " + UI.battle[UI.counter] + " <"
            UI.navmenuprint(UI.battle)

    def navup(list1, list2):
        list1[UI.counter] = list2[UI.counter]
        UI.counter = (UI.counter - 1) % len(list1)
        list1[UI.counter] = "> " + list1[UI.counter] + " <"

    def navdown(list1, list2):
        list1[UI.counter] = list2[UI.counter]
        UI.counter = (UI.counter + 1) % len(list1)
        list1[UI.counter] = "> " + list1[UI.counter] + " <"

    def menu_layout2():
        UI.draw()
        cprint("JELENLEGI POZÍCIÓ: " + variables2.biom[variables2.map[variables2.y][variables2.x]]["name"], "green", attrs=["bold"])
        UI.draw()
        cprint("NÉV: " + Character.name, "green", attrs=["bold"])
        cprint("ÉLET: " + str(Character.HP) + "/" + str(Character.HPMAX), "green", attrs=["bold"])
        cprint("SEBZÉS: " + str(Character.attack), "green", attrs=["bold"])
        cprint("GYÓGYITAL: " + str(Character.potion) + " darab", "green", attrs=["bold"])
        cprint("ELIXÍR: " + str(Character.elixir) + " darab", "green", attrs=["bold"])
        cprint("ARANY: " + str(Character.gold) + "$", "green", attrs=["bold"])

    def shoplayout():
        cprint("Üdvözöllek a boltban!", "green", attrs=["bold"])
        UI.draw()
        cprint("SEBZÉS: " + str(Character.attack), "green", attrs=["bold"])
        cprint("GYÓGYITAL: " + str(Character.potion) + " darab", "green", attrs=["bold"])
        cprint("ELIXÍR: " +str(Character.elixir) + " darab", "green", attrs=["bold"])
        cprint("ARANY: " +str(Character.gold) + "$", "green", attrs=["bold"])

    def battlelayout():
        cprint("Győzd le " + variables2.mobs [variables2.enemy] ["name"] + "-ot!", "green", attrs=["bold"])
        cprint(variables2.mobs [variables2.enemy] ["name"] + " élete: " + str(variables2.enemy_hp), "green", attrs=["bold"])
        cprint(Character.name + " élete: " + str(Character.HP) + "/" + str(Character.HPMAX), "green", attrs=["bold"])   
        cprint("GYÓGYITAL: " + str(Character.potion) + " darab", "green", attrs=["bold"])
        cprint("ELIXÍR: " +str(Character.elixir) + " darab", "green", attrs=["bold"])

    def draw():
        cprint("==============================================================================", "red")

    def logprint():
        print("\n\n\n\n\n\n\n\n\n")
        cprint("LEGUTÓBBI ESEMÉNYEK:", "green", attrs=["bold"])
        for result in variables2.loglist:
            cprint("    " + str(result), "magenta", attrs=["bold"])
    
    def navmenuprint(list):
        UI.draw()
        for i in list:
            if i == list[UI.counter]:
                cprint (i, "white", "on_magenta", attrs=["bold"])
            else:
                cprint (i, "green", attrs=["bold"])
        UI.draw()
        UI.logprint()

    def start():
        tprint("vauvau    2", "tarty1")
        tprint("PRE-ALPHA    0.0.3", "tarty1")
        cprint("NYOMJ MEG BÁRMIT AZ INDULÁSHOZ!", "green", attrs=["bold"])
        input (">")
        UI.switchstate("menu")