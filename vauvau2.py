import keyboard
from time import sleep

import variables2
from functions2 import *
import ui

start()
createmap()
os.system("cls")
draw()
ui.menu[ui.counter] = ">" + ui.menu[ui.counter] + "<"
ui.navmenuprint(ui.menu)

while True:
    while ui.state == "menu": #ÚJ JÁTÉK - JÁTÉK BETÖLTÉSE - SZABÁLYOK - KILÉPÉS
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        if keypressed == "up":
            clear()
            draw()
            ui.navup(ui.menu, ui.menu2)
            ui.navmenuprint(ui.menu)
        if keypressed == "down":
            clear()
            draw()
            ui.navdown(ui.menu, ui.menu2)
            ui.navmenuprint(ui.menu)
        if keypressed == "enter":
            if ui.counter == 0: #ÚJ JÁTÉK
                ui.switchstate("play")
            if ui.counter == 1: #JÁTÉK BETÖLTÉSE
                pass
            if ui.counter == 2: #SZABÁLYOK
                rules()
                sleep(3)
                clear()
                ui.navmenuprint(ui.menu)
            if ui.counter == 3: #KILÉPÉS
                quit()
    
    while ui.state == "play":
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass

        if keypressed == "up":
            clear()
            print_map(variables2.map2)
            ui.menu_layout2()
            ui.navup(ui.play, ui.play2)
            ui.navmenuprint(ui.play)
        if keypressed == "down":
            clear()
            print_map(variables2.map2)
            ui.menu_layout2()
            ui.navdown(ui.play, ui.play2)
            ui.navmenuprint(ui.play)
        if keypressed == "enter":
            if variables2.counter == 0: #MENTÉS ÉS KILÉPÉS
                quit()
            if variables2.counter == 1 and variables2.y > 0: #FEL
                moveup()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                ui.menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 2 and variables2.x < variables2.x_len: #JOBBRA
                moveright()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                ui.menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 3 and variables2.y < variables2.y_len: #LE
                movedown()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                ui.menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 4 and variables2.x > 0: #BALRA
                moveleft()
                spawnenemychance()
                clear()
                print_map(variables2.map2)
                ui.menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 5: #GYÓGYITAL HASZNÁLATA
                usepotion()
                clear()
                print_map(variables2.map2)
                ui.menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 6: #ELIXÍR HASZNÁLATA
                useelixir()
                clear()
                print_map(variables2.map2)
                ui.menu_layout2()
                navmenuprint(variables2.list3)
            if variables2.counter == 7: #FELSZERELÉS
                equipmentlayout()
            if variables2.counter == 8: #BELÉPÉS
                ui.switchstate(ui, "shop")

    while ui.state == "shop":
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
                ui.switchstate(ui, "play")
                variables2.loglist.clear()

    while ui.state == "battle":
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