import keyboard
from time import sleep

from ui import *
import battle
import navi
import shop
from character import *
from map import *
from variables2 import *

UI.start()
Map.createmap()

while True:
    while UI.state == "menu": #ÚJ JÁTÉK - JÁTÉK BETÖLTÉSE - SZABÁLYOK - KILÉPÉS
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down") or keyboard.is_pressed("up") or keyboard.is_pressed("enter"):
            pass

        if keypressed == "up" or keypressed == "down":
            UI.navigate(UI.menu, UI.menu2, -1 if keypressed == "up" else 1)
            os.system("cls")
            UI.navmenuprint(UI.menu)
            
        if keypressed == "enter":
            if UI.counter == 0: #ÚJ JÁTÉK
                UI.switchstate("play")
            if UI.counter == 1: #JÁTÉK BETÖLTÉSE
                pass
            if UI.counter == 2: #SZABÁLYOK
                pass
            if UI.counter == 3: #KILÉPÉS
                quit()

    while UI.state == "play":
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down") or keyboard.is_pressed("up") or keyboard.is_pressed("enter"):
            pass

        if keypressed == "up" or keypressed == "down":
            os.system("cls")
            UI.print_map(Map.map2)
            UI.menu_layout2()
            UI.navigate(UI.play, UI.play2, -1 if keypressed == "up" else 1)
            UI.navmenuprint(UI.play)

        if keypressed == "enter":
            if UI.counter == 0:
                quit()
            elif UI.counter == 1 and Character.pos_y > 0:
                navi.moveup()
            elif UI.counter == 2 and Character.pos_x < Map.len_x:
                navi.moveright()
            elif UI.counter == 3 and Character.pos_y < Map.len_y:
                navi.movedown()
            elif UI.counter == 4 and Character.pos_x > 0:
                navi.moveleft()
            elif UI.counter == 5:
                Character.usepotion()
            elif UI.counter == 6:
                Character.useelixir()
            elif UI.counter == 7:
                UI.switchstate("equipment")
            elif UI.counter == 8:
                UI.switchstate("shop")
            
            if UI.counter in [1, 2, 3, 4, 5, 6]:
                os.system("cls")
                UI.print_map(Map.map2)
                UI.menu_layout2()
                UI.navmenuprint(UI.play)
            if UI.counter in [1, 2, 3, 4]:
                battle.spawnenemychance()


    while UI.state == "shop":
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            os.system("cls")
            UI.navigate(UI.shop, UI.shop2, -1)
            UI.shoplayout()
            UI.navmenuprint(UI.shop)
        if keypressed == "down":
            os.system("cls")
            UI.navigate(UI.shop, UI.shop2, 1)
            UI.shoplayout()
            UI.navmenuprint(UI.shop)
        if keypressed == "enter":
            if UI.counter == 0:
                shop.weaponupgrade()
                os.system("cls")
                UI.shoplayout()
                UI.navmenuprint(UI.shop)
            if UI.counter == 1:
                shop.potbuy()
                os.system("cls")
                UI.shoplayout()
                UI.navmenuprint(UI.shop)
            if UI.counter == 2:
                shop.elixbuy()
                os.system("cls")
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
            os.system("cls")
            UI.navigate(UI.battle, UI.battle2, -1)
            UI.battlelayout()
            UI.navmenuprint(UI.battle)
        if keypressed == "down":
            os.system("cls")
            UI.navigate(UI.battle, UI.battle2, 1)
            UI.battlelayout()
            UI.navmenuprint(UI.battle)
        if keypressed == "enter":
            if UI.counter == 0:
                battle.attack()
                if UI.state == "battle":
                    os.system("cls")
                    UI.battlelayout()
                    UI.navmenuprint(UI.battle)
            if UI.counter == 1:
                Character.usepotion()
                os.system("cls")
                UI.battlelayout()
                UI.navmenuprint(UI.battle)
            if UI.counter == 2:
                Character.useelixir()
                os.system("cls")
                UI.battlelayout()
                UI.navmenuprint(UI.battle)
    
    while UI.state == "equipment":
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            os.system("cls")
            UI.navigate(UI.equipment, UI.equipment2, -1)
            UI.equipmentlayout()
            UI.navmenuprint(UI.equipment)
        if keypressed == "down":
            os.system("cls")
            UI.navigate(UI.equipment, UI.equipment2, 1)
            UI.equipmentlayout()
            UI.navmenuprint(UI.equipment)
        if keypressed == "enter":
            if UI.counter == 0:
                variables2.equipment_type = "weapon"
                UI.switchstate("inequipment") # FEGYVER
            if UI.counter == 1: 
                variables2.equipment_type = "armor"
                UI.switchstate("inequipment") # VÉRT
            if UI.counter == 2:
                variables2.equipment_type = "helmet"
                UI.switchstate("inequipment") # SISAK
            if UI.counter == 3:
                variables2.equipment_type = "boots"
                UI.switchstate("inequipment") # CIPŐ
            if UI.counter == 4:
                variables2.equipment_type = "talisman"
                UI.switchstate("inequipment") # TALIZMÁN
            if UI.counter == 5:
                UI.switchstate("play") # KILÉPÉS
        
    while UI.state == "inequipment":
        keypressed = keyboard.read_key()
        while keyboard.is_pressed("down"): pass
        while keyboard.is_pressed("up"): pass
        while keyboard.is_pressed("enter"): pass
        
        if keypressed == "up":
            if variables2.equipment_type == "weapon":
                UI.inequipmentup(Character.weaponbag, Character.weaponbag2)
            elif variables2.equipment_type == "armor":
                UI.inequipmentup(Character.armorbag, Character.armorbag2)
            elif variables2.equipment_type == "helmet":
                UI.inequipmentup(Character.helmetbag, Character.helmetbag2)
            elif variables2.equipment_type == "boots":
                UI.inequipmentup(Character.bootsbag, Character.bootsbag2)
            elif variables2.equipment_type == "talisman":
                UI.inequipmentup(Character.talismanbag, Character.talismanbag2)
        if keypressed == "down":
            if variables2.equipment_type == "weapon":
                UI.inequipmentdown(Character.weaponbag, Character.weaponbag2)
            elif variables2.equipment_type == "armor":
                UI.inequipmentdown(Character.armorbag, Character.armorbag2)
            elif variables2.equipment_type == "helmet":
                UI.inequipmentdown(Character.helmetbag, Character.helmetbag2)
            elif variables2.equipment_type == "boots":
                UI.inequipmentdown(Character.bootsbag, Character.bootsbag2)
            elif variables2.equipment_type == "talisman":
                UI.inequipmentdown(Character.talismanbag, Character.talismanbag2)
        if keypressed == "enter":
            if variables2.equipment_type == "weapon":
                Character.weapon = Character.weaponbag2[UI.counter]
                os.system("cls")
                UI.inequipmentlayout()
                UI.navmenuprint(Character.weaponbag)
            elif variables2.equipment_type == "armor":
                Character.armor = Character.armorbag2[UI.counter]
                os.system("cls")
                UI.inequipmentlayout()
                UI.navmenuprint(Character.armorbag)
            elif variables2.equipment_type == "helmet":
                Character.helmet = Character.helmetbag2[UI.counter]
                os.system("cls")
                UI.inequipmentlayout()
                UI.navmenuprint(Character.helmetbag)
            elif variables2.equipment_type == "boots":
                Character.boots = Character.bootsbag2[UI.counter]
                os.system("cls")
                UI.inequipmentlayout()
                UI.navmenuprint(Character.bootsbag)
            elif variables2.equipment_type == "talisman":
                Character.talisman = Character.talismanbag2[UI.counter]
                os.system("cls")
                UI.inequipmentlayout()
                UI.navmenuprint(Character.talismanbag)
            UI.switchstate("equipment")