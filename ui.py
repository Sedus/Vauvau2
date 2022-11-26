import os
import variables2
from functions2 import print_map,draw,logprint
from termcolor import cprint
from character import *

class UI:
    state = "menu"
    counter = 0
    menu = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]
    menu2 = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]
    play = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]
    play2 = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]
    shop = ["FEGYVER FEJLESZTÉSE (+2 SEBZÉS) - 10 ARANY", "GYÓGYITAL VÁSÁRLÁSA (+30HP) - 5 ARANY", "ELIXÍR VÁSÁRLÁSA (MAXHP) - 20 ARANY", "KILÉPÉS"]
    shop2 = ["FEGYVER FEJLESZTÉSE (+2 SEBZÉS) - 10 ARANY", "GYÓGYITAL VÁSÁRLÁSA (+30HP) - 5 ARANY", "ELIXÍR VÁSÁRLÁSA (MAXHP) - 20 ARANY", "KILÉPÉS"]
    battle = ["TÁMADÁS", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)"]
    battle2 = ["TÁMADÁS", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)"]
    
    def __init__(self, state, counter, menu, menu2, shop, shop2):
        self.state = state
        self.counter = counter
        self.menu = menu
        self.menu2 = menu2
        self.shop = shop
        self.shop2 = shop2

    def switchstate(self, hova):
        if hova == "menu":
            self.counter = 0
            self.state = hova
            os.system("cls")
            UI.menu_layout()
            self.menu[self.counter] = ">" + self.menu[self.counter] + "<"
            UI.navmenuprint(UI, self.menu)
        if hova == "play":
            self.counter = 0
            self.state = hova
            self.play = self.play2.copy()
            os.system("cls")
            print_map(variables2.map2)
            UI.menu_layout2()
            self.play[self.counter] = ">" + self.play[self.counter] + "<"
            UI.navmenuprint(UI, self.play)
        if hova == "shop":
            self.counter = 0
            self.state = hova
            self.shop = self.shop2.copy()
            os.system("cls")
            UI.shoplayout()
            self.shop[self.counter] = ">" + self.shop[self.counter] + "<"
            UI.navmenuprint(UI, self.shop)
        if hova == "battle":
            self.counter = 0
            self.state = hova
            self.battle = self.battle2.copy()
            os.system("cls")
            UI.battlelayout()
            self.battle[self.counter] = ">" + self.battle[self.counter] + "<"
            UI.navmenuprint(UI, self.battle)

    def navup(self, list1, list2):
        list1[self.counter] = list2[self.counter]
        self.counter = (self.counter - 1) % len(list1)
        list1[self.counter] = "> " + list1[self.counter] + " <"

    def navdown(self, list1, list2):
        list1[self.counter] = list2[self.counter]
        self.counter = (self.counter + 1) % len(list1)
        list1[self.counter] = "> " + list1[self.counter] + " <"

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

    def shoplayout():
        draw()
        cprint("Üdvözöllek a boltban!", "green", attrs=["bold"])
        draw()
        cprint("SEBZÉS: " + str(variables2.player_atk), "green", attrs=["bold"])
        cprint("GYÓGYITAL: " + str(variables2.pot) + " darab", "green", attrs=["bold"])
        cprint("ELIXÍR: " +str(variables2.elix) + " darab", "green", attrs=["bold"])
        cprint("ARANY: " +str(variables2.gold) + "$", "green", attrs=["bold"])
        draw()

    def battlelayout():
        draw()
        cprint("Győzd le " + variables2.mobs [variables2.enemy] ["name"] + "-ot!", "green", attrs=["bold"])
        draw()
        cprint(variables2.mobs [variables2.enemy] ["name"] + " élete: " + str(variables2.enemy_hp), "green", attrs=["bold"])
        cprint(variables2.name + " élete: " + str(variables2.player_hp) + "/" + str(variables2.player_hpmax), "green", attrs=["bold"])
        draw()
        cprint("GYÓGYITAL: " + str(variables2.pot) + " darab", "green", attrs=["bold"])
        cprint("ELIXÍR: " +str(variables2.elix) + " darab", "green", attrs=["bold"])
        draw()

    def navmenuprint(self, list):
        for i in list:
            if i == list[self.counter]:
                cprint (i, "white", "on_magenta", attrs=["bold"])
            else:
                cprint (i, "green", attrs=["bold"])
        logprint()