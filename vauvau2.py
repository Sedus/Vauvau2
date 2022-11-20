from art import tprint
from termcolor import cprint
import keyboard
from time import sleep

import variables2
from functions2 import *

start()
createmap()
draw()
variables2.list[variables2.counter] = ">" + variables2.list[variables2.counter] + "<"
navmenuprint(variables2.list)

while True:
    while variables2.menu: #ÚJ JÁTÉK - JÁTÉK BETÖLTÉSE - SZABÁLYOK - KILÉPÉS
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        if keypressed == "up":
            clear()
            draw()
            navup(variables2.list, variables2.list2)
            navmenuprint(variables2.list)
        if keypressed == "down":
            clear()
            draw()
            navdown(variables2.list, variables2.list2)
            navmenuprint(variables2.list)
        if keypressed == "enter":
            if variables2.counter == 0: #ÚJ JÁTÉK
                toplay()
            if variables2.counter == 1: #JÁTÉK BETÖLTÉSE
                pass
            if variables2.counter == 2: #SZABÁLYOK
                rules()
                sleep(3)
                clear()
                navmenuprint(variables2.list)
            if variables2.counter == 3: #KILÉPÉS
                quit()
    
    while variables2.play:
        if variables2.bool1:
            clear()
            print_map(variables2.map2)
            menu_layout2()
            variables2.list3[variables2.counter] = ">" + variables2.list3[variables2.counter] + "<"
            navmenuprint(variables2.list3)
            variables2.bool1 = False

        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass

        if keypressed == "up":
            clear()
            print_map(variables2.map2)
            menu_layout2()
            navup(variables2.list3, variables2.list4)
            navmenuprint(variables2.list3)
        if keypressed == "down":
            clear()
            print_map(variables2.map2)
            menu_layout2()
            navdown(variables2.list3, variables2.list4)
            navmenuprint(variables2.list3)
        if keypressed == "enter":
            if variables2.counter == 0: #MENTÉS ÉS KILÉPÉS
                quit()
            if variables2.counter == 1 and variables2.y > 0: #FEL
                moveup()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 2 and variables2.x < variables2.x_len: #JOBBRA
                moveright()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 3 and variables2.y < variables2.y_len: #LE
                movedown()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 4 and variables2.x > 0: #BALRA
                moveleft()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 5: #GYÓGYITAL HASZNÁLATA
                usepotion()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 6: #ELIXÍR HASZNÁLATA
                useelixir()
                clear()
                print_map(variables2.map2)
                menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 7: #FELSZERELÉS
                equipmentlayout()
            if variables2.counter == 8: #BELÉPÉS
                toshop()

    while variables2.shop:
        if variables2.bool3:
            clear()
            shoplayout()
            variables2.list7[variables2.counter] = ">" + variables2.list7[variables2.counter] + "<"
            navmenuprint(variables2.list7)
            variables2.bool3 = False
        
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            clear()
            shoplayout()
            navup(variables2.list7, variables2.list8)
            navmenuprint(variables2.list7)
        if keypressed == "down":
            clear()
            shoplayout()
            navdown(variables2.list7, variables2.list8)
            navmenuprint(variables2.list7)
        if keypressed == "enter":
            if variables2.counter == 0:
                weaponupgrade()
                clear()
                shoplayout()
                navmenuprint(variables2.list7)
            if variables2.counter == 1:
                potbuy()
                clear()
                shoplayout()
                navmenuprint(variables2.list7)
            if variables2.counter == 2:
                elixbuy()
                clear()
                shoplayout()
                navmenuprint(variables2.list7)
            if variables2.counter == 3: #KILÉPÉS
                toplay()
                variables2.loglist.clear()

    while variables2.battle:
        if variables2.bool2:
            clear()
            battlelayout()
            variables2.list5[variables2.counter] = ">" + variables2.list5[variables2.counter] + "<"
            navmenuprint(variables2.list5)
            variables2.bool2 = False

        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            clear()
            battlelayout()
            navup(variables2.list5, variables2.list6)
            navmenuprint(variables2.list5)
        if keypressed == "down":
            clear()
            battlelayout()
            navdown(variables2.list5, variables2.list6)
            navmenuprint(variables2.list5)
        if keypressed == "enter":
            if variables2.counter == 0:
                attack()
                clear()
                battlelayout()
                navmenuprint(variables2.list5)
            if variables2.counter == 1:
                usepotion()
                clear()
                battlelayout()
                navmenuprint(variables2.list5)
            if variables2.counter == 2:
                useelixir()
                clear()
                battlelayout()
                navmenuprint(variables2.list5)
    
    while variables2.equipment:
        equipmentlayout()

        choice = input("# ")

        if choice == "1":
            pass
        if choice == "2":
            pass
        if choice == "3":
            pass