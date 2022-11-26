import keyboard
from time import sleep

import variables2
from functions2 import *
from ui import *
import battle

UI.start()
createmap()

while True:
    while UI.state == "menu": #ÚJ JÁTÉK - JÁTÉK BETÖLTÉSE - SZABÁLYOK - KILÉPÉS
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            clear()
            UI.navup(UI.menu, UI.menu2)
            UI.navmenuprint(UI.menu)
        if keypressed == "down":
            clear()
            UI.navdown(UI.menu, UI.menu2)
            UI.navmenuprint(UI.menu)
        if keypressed == "enter":
            if UI.counter == 0: #ÚJ JÁTÉK
                UI.switchstate("play")
            if UI.counter == 1: #JÁTÉK BETÖLTÉSE
                pass
            if UI.counter == 2: #SZABÁLYOK
                rules()
                sleep(3)
                clear()
                UI.navmenuprint(UI.menu)
            if UI.counter == 3: #KILÉPÉS
                quit()
    
    while UI.state == "play":
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass

        if keypressed == "up":
            clear()
            print_map(variables2.map2)
            UI.menu_layout2()
            UI.navup(UI.play, UI.play2)
            UI.navmenuprint(UI.play)
        if keypressed == "down":
            clear()
            print_map(variables2.map2)
            UI.menu_layout2()
            UI.navdown(UI.play, UI.play2)
            UI.navmenuprint(UI.play)
        if keypressed == "enter":
            if UI.counter == 0: #MENTÉS ÉS KILÉPÉS
                quit()
            if UI.counter == 1 and variables2.y > 0: #FEL
                moveup()
                clear()
                print_map(variables2.map2)
                UI.menu_layout2()
                UI.navmenuprint(UI.play)
                battle.spawnenemychance()
            if UI.counter == 2 and variables2.x < variables2.x_len: #JOBBRA
                moveright()
                clear()
                print_map(variables2.map2)
                UI.menu_layout2()
                UI.navmenuprint(UI.play)
                battle.spawnenemychance()
            if UI.counter == 3 and variables2.y < variables2.y_len: #LE
                movedown()
                clear()
                print_map(variables2.map2)
                UI.menu_layout2()
                UI.navmenuprint(UI.play)
                battle.spawnenemychance()
            if UI.counter == 4 and variables2.x > 0: #BALRA
                moveleft()
                clear()
                print_map(variables2.map2)
                UI.menu_layout2()
                UI.navmenuprint(UI.play)
                battle.spawnenemychance()
            if UI.counter == 5: #GYÓGYITAL HASZNÁLATA
                usepotion()
                clear()
                print_map(variables2.map2)
                UI.menu_layout2()
                UI.navmenuprint(UI.play)
            if UI.counter == 6: #ELIXÍR HASZNÁLATA
                useelixir()
                clear()
                print_map(variables2.map2)
                UI.menu_layout2()
                UI.navmenuprint(UI.play)
            if UI.counter == 7: #FELSZERELÉS
                equipmentlayout()
            if UI.counter == 8: #BELÉPÉS
                UI.switchstate("shop")

    while UI.state == "shop":
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            clear()
            UI.shoplayout()
            UI.navup(UI.shop, UI.shop2)
            UI.navmenuprint(UI.shop)
        if keypressed == "down":
            clear()
            UI.shoplayout()
            UI.navdown(UI.shop, UI.shop2)
            UI.navmenuprint(UI.shop)
        if keypressed == "enter":
            if UI.counter == 0:
                weaponupgrade()
                clear()
                UI.shoplayout()
                UI.navmenuprint(UI.shop)
            if UI.counter == 1:
                potbuy()
                clear()
                UI.shoplayout()
                UI.navmenuprint(UI.shop)
            if UI.counter == 2:
                elixbuy()
                clear()
                UI.shoplayout()
                UI.navmenuprint(UI.shop)
            if UI.counter == 3: #KILÉPÉS
                UI.switchstate("play")

    while UI.state == "battle":
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            clear()
            UI.battlelayout()
            UI.navup(UI.battle, UI.battle2)
            UI.navmenuprint(UI.battle)
        if keypressed == "down":
            clear()
            UI.battlelayout()
            UI.navdown(UI.battle, UI.battle2)
            UI.navmenuprint(UI.battle)
        if keypressed == "enter":
            if UI.counter == 0:
                battle.attack()
                if UI.state == "battle":
                    clear()
                    UI.battlelayout()
                    UI.navmenuprint(UI.battle)
            if UI.counter == 1:
                usepotion()
                clear()
                UI.battlelayout()
                UI.navmenuprint(UI.battle)
            if UI.counter == 2:
                useelixir()
                clear()
                UI.battlelayout()
                UI.navmenuprint(UI.battle)