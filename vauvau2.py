from art import tprint
from termcolor import cprint
import keyboard
from time import sleep

import variables2
from functions2 import *

start()
createmap()

counter = 0

variables2.list[counter] = ">" + variables2.list[counter] + "<"
for i in variables2.list:
    cprint(i, "green")

while True:
    while variables2.menu: #ÚJ JÁTÉK - JÁTÉK BETÖLTÉSE - SZABÁLYOK - KILÉPÉS
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            clear()
            variables2.list[counter] = variables2.list2[counter]
            counter -= 1
            variables2.list[counter] = "> " + variables2.list[counter] + " <"
            for i in variables2.list:
                cprint (i, "green")
        if keypressed == "down":
            clear()
            variables2.list[counter] = variables2.list2[counter]
            counter += 1
            variables2.list[counter] = "> " + variables2.list[counter] + " <"
            for i in variables2.list:
                cprint (i, "green")
        if keypressed == "enter":
            if counter == 0: #ÚJ JÁTÉK
                toplay()
            if counter == 1: #JÁTÉK BETÖLTÉSE
                pass
            if counter == 2: #SZABÁLYOK
                rules()
                sleep(3)
                clear()
                for i in variables2.list:
                    cprint (i, "green")
            if counter == 3: #KILÉPÉS
                quit()
    
    while variables2.play:
        if bool:
            clear()
            print_map(variables2.map2)
            menu_layout2()
            variables2.list3[counter] = ">" + variables2.list3[counter] + "<"
            navmenuprint(variables2.list3)
            bool = False

            
        # counter is 0
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            clear()
            print_map(variables2.map2)
            menu_layout2()
            variables2.list3[counter] = variables2.list4[counter]
            counter -= 1
            variables2.list3[counter] = "> " + variables2.list3[counter] + " <"
            navmenuprint(variables2.list3)
        if keypressed == "down":
            clear()
            print_map(variables2.map2)
            menu_layout2()
            variables2.list3[counter] = variables2.list4[counter]
            counter += 1
            variables2.list3[counter] = "> " + variables2.list3[counter] + " <"
            navmenuprint(variables2.list3)
        if keypressed == "enter":
            if counter == 0: #MENTÉS ÉS KILÉPÉS
                quit()
            if counter == 1 and variables2.y > 0: #FEL
                moveup()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if counter == 2 and variables2.x < variables2.x_len: #JOBBRA
                moveright()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if counter == 3 and variables2.y < variables2.y_len: #LE
                movedown()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if counter == 4 and variables2.x > 0: #BALRA
                moveleft()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if counter == 5: #GYÓGYITAL HASZNÁLATA
                usepotion()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if counter == 6: #ELIXÍR HASZNÁLATA
                useelixir()
            if counter == 7: #BELÉPÉS
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

    while variables2.equipment:
        equipmentlayout()

        choice = input("# ")

        if choice == "1":
            pass
        if choice == "2":
            pass
        if choice == "3":
            pass