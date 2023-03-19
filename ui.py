import os
from variables2 import *
from termcolor import cprint
from art import tprint
from character import *
from map import *
from enemy import *
from items import *

class UI:
    def __init__(self, state, counter, menu, menu2, play, play2, shop, shop2, battle, battle2, equipment, equipment2):
        self.state = state
        self.counter = counter
        self.menu = menu
        self.menu2 = menu2
        self.play = play
        self.play2 = play2
        self.shop = shop
        self.shop2 = shop2
        self.battle = battle
        self.battle2 = battle2
        self.equipment = equipment
        self.equipment2 = equipment2

    def switchstate(hova):
        if hova == "menu":
            UI.counter = 0
            UI.state = hova
            UI.menu = UI.menu2.copy()
            os.system("cls")
            UI.menu[UI.counter] = "> " + UI.menu[UI.counter] + " <"
            UI.navmenuprint(UI.menu)
        if hova == "play":
            Character.stat_calc(Character)
            UI.counter = 0
            UI.state = hova
            UI.play = UI.play2.copy()
            os.system("cls")
            UI.print_map(Map.map2)
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
            variables2.loglist.clear()
            os.system("cls")
            UI.battlelayout()
            UI.battle[UI.counter] = "> " + UI.battle[UI.counter] + " <"
            UI.navmenuprint(UI.battle)
        if hova == "equipment":
            UI.counter = 0
            UI.state = hova
            UI.equipment = UI.equipment2.copy()
            variables2.loglist.clear()
            os.system("cls")
            UI.equipmentlayout()
            UI.equipment[UI.counter] = "> " + UI.equipment[UI.counter] + " <"
            UI.navmenuprint(UI.equipment)
        if hova == "inequipment":
            Character.weaponbag = [i[1] for i in sorted(((i[1]["attack"],i[0]) for i in weapon.items() if i[0] in set(Character.weaponbag)))]
            Character.weaponbag2 = [i[1] for i in sorted(((i[1]["attack"],i[0]) for i in weapon.items() if i[0] in set(Character.weaponbag2)))]
            Character.armorbag = [i[1] for i in sorted(((i[1]["armor"],i[0]) for i in armor.items() if i[0] in set(Character.armorbag)))]
            Character.armorbag2 = [i[1] for i in sorted(((i[1]["armor"],i[0]) for i in armor.items() if i[0] in set(Character.armorbag2)))]
            Character.helmetbag = [i[1] for i in sorted(((i[1]["HP"],i[0]) for i in helmet.items() if i[0] in set(Character.helmetbag)))]
            Character.helmetbag2 = [i[1] for i in sorted(((i[1]["HP"],i[0]) for i in helmet.items() if i[0] in set(Character.helmetbag2)))]
            Character.bootsbag = [i[1] for i in sorted(((i[1]["HP"],i[0]) for i in boots.items() if i[0] in set(Character.bootsbag)))]
            Character.bootsbag2 = [i[1] for i in sorted(((i[1]["HP"],i[0]) for i in boots.items() if i[0] in set(Character.bootsbag2)))]
            Character.talismanbag = [i[1] for i in sorted(((i[1]["attack"],i[0]) for i in talisman.items() if i[0] in set(Character.talismanbag)))]
            Character.talismanbag2 = [i[1] for i in sorted(((i[1]["attack"],i[0]) for i in talisman.items() if i[0] in set(Character.talismanbag2)))]
            UI.counter = 0
            UI.state = hova
            variables2.loglist.clear()
            os.system("cls")
            UI.inequipmentlayout()
            if variables2.equipment_type == "weapon":
                Character.weaponbag =  Character.weaponbag2.copy()
                Character.weaponbag[UI.counter] = "> " +  Character.weaponbag[UI.counter] + " <"
                UI.navmenuprint(Character.weaponbag)
            elif variables2.equipment_type == "armor":
                Character.armorbag =  Character.armorbag2.copy()
                Character.armorbag[UI.counter] = "> " +  Character.armorbag[UI.counter] + " <"
                UI.navmenuprint(Character.armorbag)
            elif variables2.equipment_type == "helmet":
                Character.helmetbag =  Character.helmetbag2.copy()
                Character.helmetbag[UI.counter] = "> " +  Character.helmetbag[UI.counter] + " <"
                UI.navmenuprint(Character.helmetbag)
            elif variables2.equipment_type == "boots":
                Character.bootsbag =  Character.bootsbag2.copy()
                Character.bootsbag[UI.counter] = "> " +  Character.bootsbag[UI.counter] + " <"
                UI.navmenuprint(Character.bootsbag)
            elif variables2.equipment_type == "talisman":
                Character.talismanbag =  Character.talismanbag2.copy()
                Character.talismanbag[UI.counter] = "> " +  Character.talismanbag[UI.counter] + " <"
                UI.navmenuprint(Character.talismanbag)

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
        cprint("JELENLEGI POZÍCIÓ: " + Map.biom[Map.map[Character.pos_y][Character.pos_x]]["name"], "green", attrs=["bold"])
        UI.draw()
        cprint("NÉV: " + Character.name + " " * (50 - len("NÉV: " + Character.name)) + "FEGYVER: " + Character.weapon, "green", attrs=["bold"])
        cprint("ÉLET: " + str(Character.HP) + "/" + str(Character.HPMAX) + " " * (50 - len("ÉLET: " + str(Character.HP) + "/" + str(Character.HPMAX))) + "VÉRT: " + Character.armor, "green", attrs=["bold"])
        cprint("SEBZÉS: " + str(Character.attack) + " " * (50 - len(str("SEBZÉS: " + str(Character.attack)))) + "SISAK: " + Character.helmet, "green", attrs=["bold"])
        cprint("PÁNCÉL: " + str(Character.defense) + " " * (50 - len(str("PÁNCÉL: " + str(Character.defense)))) + "CIPŐ: " + Character.boots, "green", attrs=["bold"])
        cprint("GYÓGYITAL: " + str(Character.potion) + " darab" + " " * (50 - len(str("GYÓGYITAL: " + str(Character.potion) + " darab"))) + "TALIZMÁN: " + Character.talisman, "green", attrs=["bold"])
        cprint("ELIXÍR: " + str(Character.elixir) + " darab", "green", attrs=["bold"])
        cprint("ARANY: " + str(Character.gold) + "$", "green", attrs=["bold"])

    def shoplayout():
        cprint("""
                (
        
                )
                ( _   _._
                |_|-'_~_`-._
            _.-'-_~_-~_-~-_`-._
        _.-'_~-_~-_-~-_~_~-_~-_`-._
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            |  []  []   []   []  [] |
            |           __    ___   |   
        ._|  []  []  | .|  [___]  |_._._._._._._._._._._._._._._._._.  
        |=|________()|__|()_______|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=| 
        ^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
                          ===   
                            === 
                              ===
                                ===
        """, "white", attrs=["bold"])
        UI.draw()
        cprint("ÉLET: " + str(Character.HP) + "/" + str(Character.HPMAX), "green", attrs=["bold"])
        cprint("SEBZÉS: " + str(Character.attack), "green", attrs=["bold"])
        cprint("PÁNCÉL: " + str(Character.defense), "green", attrs=["bold"])
        cprint("GYÓGYITAL: " + str(Character.potion) + " darab", "green", attrs=["bold"])
        cprint("ELIXÍR: " + str(Character.elixir) + " darab", "green", attrs=["bold"])
        cprint("ARANY: " + str(Character.gold) + "$", "green", attrs=["bold"])

    def battlelayout():
        if isinstance(Enemy.selected_enemy, Orc):
            UI.orc_print()
        if isinstance(Enemy.selected_enemy, Goblin):
            UI.orc_print()
        if isinstance(Enemy.selected_enemy, Slime):
            UI.orc_print()
        UI.draw()
        cprint(Enemy.selected_enemy.name, "white", "on_blue", attrs=["bold"])
        cprint("ÉLET: " + str(Enemy.selected_enemy.HP) + "/" + str(Enemy.selected_enemy.HPMAX), "green", attrs=["bold"])
        cprint("SEBZÉS: " + str(Enemy.selected_enemy.attack), "green", attrs=["bold"])
        cprint("PÁNCÉL: " + str(Enemy.selected_enemy.defense), "green", attrs=["bold"])
        UI.draw()
        cprint(Character.name, "white", "on_blue", attrs=["bold"])
        cprint("ÉLET: " + str(Character.HP) + "/" + str(Character.HPMAX), "green", attrs=["bold"])
        cprint("SEBZÉS: " + str(Character.attack), "green", attrs=["bold"])
        cprint("PÁNCÉL: " + str(Character.defense), "green", attrs=["bold"])
        cprint("GYÓGYITAL: " + str(Character.potion) + " darab", "green", attrs=["bold"])
        cprint("ELIXÍR: " + str(Character.elixir) + " darab", "green", attrs=["bold"])
        cprint("ARANY: " + str(Character.gold) + "$", "green", attrs=["bold"])

    def equipmentlayout():
        cprint("""
                           .-.
                          {{#}}
          {}               8@8
        .::::.             888
    @\\/W\/\/W\//@         8@8
     \\/^\/\/^\//     _    )8(    _
      \_O_{}_O_/     (@)__/8@8\__(@)
 ____________________ `~"-=):(=-"~`
|<><><>  |  |  <><><>|     |.|
|<>      |  |      <>|     |S|
|<>      |  |      <>|     |'|
|<>   .--------.   <>|     |.|
|     |   ()   |     |     |P|
|_____| (O\/O) |_____|     |'|
|     \   /\   /     |     |.|
|------\  \/  /------|     |U|
|       '.__.'       |     |'|
|        |  |        |     |.|
:        |  |        :     |N|
 \       |  |       /      |'|
  \<>    |  |    <>/       |.|
   \<>   |  |   <>/        |K|
    `\<> |  | <>/'         |'|
      `-.|__|.-`           \ /
                            ˇ
        """, "green", attrs=["bold"])
        UI.draw()
        cprint("FEGYVER: " + Character.weapon, "green", attrs=["bold"])
        cprint("VÉRT: " + Character.armor, "green", attrs=["bold"])
        cprint("SISAK: " + Character.helmet, "green", attrs=["bold"])
        cprint("CIPŐ: " + Character.boots, "green", attrs=["bold"])
        cprint("TALIZMÁN: " + Character.talisman, "green", attrs=["bold"])

    def inequipmentlayout():
        cprint("Felszerelt tárgy:                                 Kiválasztott tárgy:\n", "green", attrs=["bold"])
        if variables2.equipment_type == "weapon":
            cprint(Character.weapon + " " * (50 - len(Character.weapon)) + Character.weaponbag2[UI.counter], "green", attrs=["bold"])
            cprint("SEBZÉS: " + str(weapon[Character.weapon]["attack"]) + " " * (42 - len(str(weapon[Character.weapon]["attack"]))) + "SEBZÉS: " + str(weapon[Character.weaponbag2[UI.counter]]["attack"]), "green", attrs=["bold"])
        elif variables2.equipment_type == "armor":
            cprint(Character.armor + " " * (50 - len(Character.armor)) + Character.armorbag2[UI.counter], "green", attrs=["bold"])
            cprint("PÁNCÉL: " + str(armor[Character.armor]["armor"]) + " " * (42 - len(str(armor[Character.armor]["armor"]))) + "PÁNCÉL: " + str(armor[Character.armorbag2[UI.counter]]["armor"]), "green", attrs=["bold"])
        elif variables2.equipment_type == "helmet":
            cprint(Character.helmet + " " * (50 - len(Character.helmet)) + Character.helmetbag2[UI.counter], "green", attrs=["bold"])
            cprint("HP: " + str(helmet[Character.helmet]["HP"]) + " " * (46 - len(str(helmet[Character.helmet]["HP"]))) + "HP: " + str(helmet[Character.helmetbag2[UI.counter]]["HP"]), "green", attrs=["bold"])
        elif variables2.equipment_type == "boots":
            cprint(Character.boots + " " * (50 - len(Character.boots)) + Character.bootsbag2[UI.counter], "green", attrs=["bold"])
            cprint("HP: " + str(boots[Character.boots]["HP"]) + " " * (46 - len(str(boots[Character.boots]["HP"]))) + "HP: " + str(boots[Character.bootsbag2[UI.counter]]["HP"]), "green", attrs=["bold"])
        elif variables2.equipment_type == "talisman":
            cprint(Character.talisman + " " * (50 - len(Character.talisman)) + Character.talismanbag2[UI.counter], "green", attrs=["bold"])
            cprint("SEBZÉS: " + str(talisman[Character.talisman]["attack"]) + " " * (42 - len(str(talisman[Character.talisman]["attack"]))) + "SEBZÉS: " + str(talisman[Character.talismanbag2[UI.counter]]["attack"]), "green", attrs=["bold"])
            cprint("PÁNCÉL: " + str(talisman[Character.talisman]["armor"]) + " " * (42 - len(str(talisman[Character.talisman]["armor"]))) + "PÁNCÉL: " + str(talisman[Character.talismanbag2[UI.counter]]["armor"]), "green", attrs=["bold"])
            cprint("HP: " + str(talisman[Character.talisman]["HP"]) + " " * (46 - len(str(talisman[Character.talisman]["HP"]))) + "HP: " + str(talisman[Character.talismanbag2[UI.counter]]["HP"]), "green", attrs=["bold"])

    def inequipmentup(list1, list2):
        os.system("cls")
        UI.navup(list1, list2)
        UI.inequipmentlayout()
        UI.navmenuprint(list1)
    
    def inequipmentdown(list1, list2):
        os.system("cls")
        UI.navdown(list1, list2)
        UI.inequipmentlayout()
        UI.navmenuprint(list1)

    def draw():
        cprint("=" * 78, "red")

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
        tprint("PRE-ALPHA    0.5.0", "tarty1")
        cprint("NYOMJ MEG BÁRMIT AZ INDULÁSHOZ!", "green", attrs=["bold"])
        input (">")
        UI.switchstate("menu")
    
    def rules():
        cprint("\nFel-le nyíllal tudsz navigálni." + "\n" + "Enter lenyomásával kiválasztod az adott utasítást.", "green", attrs=["bold"])

    def tiledraw():
        icon =  Map.biom [Map.map[Character.pos_y][Character.pos_x]] ["icon"]
        Map.map2[Character.pos_y][Character.pos_x] = icon

    def print_map(map2):
        for i in map2:
            cprint('\n' + '+---' * 7 + '+', "red")
            for j in i:
                cprint('| ', "red", end='')
                cprint(format(j) + " ", "green", attrs=["bold"], end='')
            cprint('|', "red", end='')
        cprint('\n' + '+---' * 7 + '+', "red")
    
    def orc_print():
        cprint("""                                                                                                                                        
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
    """, "green", attrs=["bold"])

UI.state = None
UI.counter = 0
UI.menu = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]
UI.menu2 = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]
UI.play = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]
UI.play2 = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]
UI.shop = ["FEGYVER FEJLESZTÉSE (+2 SEBZÉS) - 10 ARANY", "GYÓGYITAL VÁSÁRLÁSA (+30HP) - 5 ARANY", "ELIXÍR VÁSÁRLÁSA (MAXHP) - 20 ARANY", "KILÉPÉS"]
UI.shop2 = ["FEGYVER FEJLESZTÉSE (+2 SEBZÉS) - 10 ARANY", "GYÓGYITAL VÁSÁRLÁSA (+30HP) - 5 ARANY", "ELIXÍR VÁSÁRLÁSA (MAXHP) - 20 ARANY", "KILÉPÉS"]
UI.battle = ["TÁMADÁS", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)"]
UI.battle2 = ["TÁMADÁS", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)"]
UI.equipment = ["FEGYVER", "VÉRT", "SISAK", "CIPŐ", "TALIZMÁN", "KILÉPÉS"]
UI.equipment2 = ["FEGYVER", "VÉRT", "SISAK", "CIPŐ", "TALIZMÁN", "KILÉPÉS"]