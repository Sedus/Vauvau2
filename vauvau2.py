from art import tprint
from time import sleep
from termcolor import cprint

import variables2
from functions2 import *

start()
createmap()

while True:
    while variables2.menu: #ÚJ JÁTÉK - JÁTÉK BETÖLTÉSE - SZABÁLYOK - KILÉPÉS
        menu_layout()
        choice = input("# ")

        if choice == "1": #ÚJ JÁTÉK
            toplay()
        elif choice == "2": #JÁTÉK BETÖLTÉSE
            pass
        elif choice == "3": #SZABÁLYOK
            rules()
        elif choice == "4": #KILÉPÉS
            quit()

    while variables2.play:
        print_map(variables2.map2)
        #print(variables2.map) #debug only
        menu_layout2()
        choice = input("# ")

        if choice == "0": #MENTÉS ÉS KILÉPÉS
            quit()
        elif choice == "1": #FEL
            moveup()
            spawnenemychance()
        elif choice == "2": #JOBBRA
            moveright()
            spawnenemychance()
        elif choice == "3": #LE
            movedown()
            spawnenemychance()
        elif choice == "4": #BALRA
            moveleft()
            spawnenemychance()
        elif choice == "5": #GYÓGYITAL HASZNÁLATA
            usepotion()
        elif choice == "6": #ELIXÍR HASZNÁLATA
            useelixir()
        elif choice == "7": #BELÉPÉS
            toshop()

    while variables2.shop:
        shoplayout()
        choice = input("# ")
        
        if choice == "1":
            weaponupgrade()
        elif choice == "2":
            potbuy()
        elif choice == "3":
            elixbuy()
        elif choice == "4":
            toplay()

    while variables2.battle:
        battlelayout()
        choice = input("# ")

        if choice == "1":
            attack()
        if choice == "2":
            usepotion()
        if choice == "3":
            useelixir()