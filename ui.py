import os
from variables2 import *
from termcolor import cprint
from art import tprint
from character import *
from map import *
from enemy import *
from items import *

class UI:
    def __init__(self, state, counter, menu, menu2, play, play2, shop, shop2, battle, battle2, equipment, equipment2, itemlist, itemlist2):
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
        self.itemlist = itemlist
        self.itemlist2 = itemlist2

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
            UI.state = hova
            Character.weaponbag =  Character.weaponbag2.copy()
            variables2.loglist.clear()
            os.system("cls")
            UI.inequipmentlayout()
            Character.weaponbag[UI.counter] = "> " +  Character.weaponbag[UI.counter] + " <"
            UI.navmenuprint(Character.weaponbag)

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
        cprint("JELENLEGI POZ??CI??: " + Map.biom[Map.map[Character.pos_y][Character.pos_x]]["name"], "green", attrs=["bold"])
        UI.draw()
        cprint("N??V: " + Character.name, "green", attrs=["bold"])
        cprint("??LET: " + str(Character.HP) + "/" + str(Character.HPMAX), "green", attrs=["bold"])
        cprint("SEBZ??S: " + str(Character.attack), "green", attrs=["bold"])
        cprint("P??NC??L: " + str(Character.defense), "green", attrs=["bold"])
        cprint("GY??GYITAL: " + str(Character.potion) + " darab", "green", attrs=["bold"])
        cprint("ELIX??R: " + str(Character.elixir) + " darab", "green", attrs=["bold"])
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
        cprint("??LET: " + str(Character.HP) + "/" + str(Character.HPMAX), "green", attrs=["bold"])
        cprint("SEBZ??S: " + str(Character.attack), "green", attrs=["bold"])
        cprint("P??NC??L: " + str(Character.defense), "green", attrs=["bold"])
        cprint("GY??GYITAL: " + str(Character.potion) + " darab", "green", attrs=["bold"])
        cprint("ELIX??R: " + str(Character.elixir) + " darab", "green", attrs=["bold"])
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
        cprint("??LET: " + str(Enemy.selected_enemy.HP) + "/" + str(Enemy.selected_enemy.HPMAX), "green", attrs=["bold"])
        cprint("SEBZ??S: " + str(Enemy.selected_enemy.attack), "green", attrs=["bold"])
        cprint("P??NC??L: " + str(Enemy.selected_enemy.defense), "green", attrs=["bold"])
        UI.draw()
        cprint(Character.name, "white", "on_blue", attrs=["bold"])
        cprint("??LET: " + str(Character.HP) + "/" + str(Character.HPMAX), "green", attrs=["bold"])
        cprint("SEBZ??S: " + str(Character.attack), "green", attrs=["bold"])
        cprint("P??NC??L: " + str(Character.defense), "green", attrs=["bold"])
        cprint("GY??GYITAL: " + str(Character.potion) + " darab", "green", attrs=["bold"])
        cprint("ELIX??R: " + str(Character.elixir) + " darab", "green", attrs=["bold"])
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
                            ??
        """, "green", attrs=["bold"])
        UI.draw()
        cprint("FEGYVER: " + Character.weapon, "green", attrs=["bold"])
        cprint("V??RT: " + Character.armor, "green", attrs=["bold"])
        cprint("SISAK: " + Character.helmet, "green", attrs=["bold"])
        cprint("CIP??: " + Character.boots, "green", attrs=["bold"])
        cprint("TALIZM??N: " + Character.talisman, "green", attrs=["bold"])

    def inequipmentlayout():
        cprint("Felszerelt t??rgy:                                 Kiv??lasztott t??rgy:\n", "green", attrs=["bold"])
        if variables2.equipment_type == "weapon":
            cprint(Character.weapon + "                                         " + Character.weaponbag2[UI.counter], "green", attrs=["bold"])
            cprint("SEBZ??S: " + str(weapon[Character.weapon]["attack"]) + "                                        " + "SEBZ??S: " + str(weapon[Character.weaponbag2[UI.counter]]["attack"]), "green", attrs=["bold"])
        elif variables2.equipment_type == "armor":
            cprint(Character.armor + "                                         " + Character.armorbag2[UI.counter], "green", attrs=["bold"])
            cprint("P??NC??L: " + str(armor[Character.armor]["armor"]) + "                                        " + "P??NC??L: " + str(armor[Character.armorbag2[UI.counter]]["armor"]), "green", attrs=["bold"])
        elif variables2.equipment_type == "helmet":
            cprint(Character.weapon + "                                         " + UI.inequipment2[UI.counter], "green", attrs=["bold"])
            cprint("SEBZ??S: " + str(weapon[Character.weapon]["attack"]) + "                                        " + "SEBZ??S: " + str(weapon[UI.inequipment2[UI.counter]]["attack"]), "green", attrs=["bold"])
            cprint(Character.helmet, "green", attrs=["bold"])
            cprint("HP: " + str(helmet[Character.helmet]["HP"]), "green", attrs=["bold"])
        elif variables2.equipment_type == "boots":
            cprint(Character.weapon + "                                         " + UI.inequipment2[UI.counter], "green", attrs=["bold"])
            cprint("SEBZ??S: " + str(weapon[Character.weapon]["attack"]) + "                                        " + "SEBZ??S: " + str(weapon[UI.inequipment2[UI.counter]]["attack"]), "green", attrs=["bold"])
            cprint(Character.boots, "green", attrs=["bold"])
            cprint("HP: " + str(boots[Character.boots]["HP"]), "green", attrs=["bold"])
        elif variables2.equipment_type == "talisman":
            cprint(Character.talisman, "green", attrs=["bold"])
            cprint("SEBZ??S: " + str(talisman[Character.talisman]["attack"]), "green", attrs=["bold"])
            cprint("P??NC??L: " + str(talisman[Character.talisman]["armor"]), "green", attrs=["bold"])
            cprint("HP: " + str(talisman[Character.talisman]["HP"]), "green", attrs=["bold"])

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
        cprint("==============================================================================", "red")

    def logprint():
        print("\n\n\n\n\n\n\n\n\n")
        cprint("LEGUT??BBI ESEM??NYEK:", "green", attrs=["bold"])
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
        tprint("PRE-ALPHA    0.3.0", "tarty1")
        cprint("NYOMJ MEG B??RMIT AZ INDUL??SHOZ!", "green", attrs=["bold"])
        input (">")
        UI.switchstate("menu")
    
    def rules():
        cprint("\nFel-le ny??llal tudsz navig??lni." + "\n" + "Enter lenyom??s??val kiv??lasztod az adott utas??t??st.", "green", attrs=["bold"])

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
UI.menu = ["??J J??T??K", "J??T??K BET??LT??SE", "SZAB??LYOK", "KIL??P??S"]
UI.menu2 = ["??J J??T??K", "J??T??K BET??LT??SE", "SZAB??LYOK", "KIL??P??S"]
UI.play = ["MENT??S ??S KIL??P??S", "??? FEL", "??? JOBBRA", "??? LE", "??? BALRA", "GY??GYITAL HASZN??LATA (30HP)", "ELIX??R HASZN??LATA (MAXHP)", "FELSZEREL??S", "BEL??P??S"]
UI.play2 = ["MENT??S ??S KIL??P??S", "??? FEL", "??? JOBBRA", "??? LE", "??? BALRA", "GY??GYITAL HASZN??LATA (30HP)", "ELIX??R HASZN??LATA (MAXHP)", "FELSZEREL??S", "BEL??P??S"]
UI.shop = ["FEGYVER FEJLESZT??SE (+2 SEBZ??S) - 10 ARANY", "GY??GYITAL V??S??RL??SA (+30HP) - 5 ARANY", "ELIX??R V??S??RL??SA (MAXHP) - 20 ARANY", "KIL??P??S"]
UI.shop2 = ["FEGYVER FEJLESZT??SE (+2 SEBZ??S) - 10 ARANY", "GY??GYITAL V??S??RL??SA (+30HP) - 5 ARANY", "ELIX??R V??S??RL??SA (MAXHP) - 20 ARANY", "KIL??P??S"]
UI.battle = ["T??MAD??S", "GY??GYITAL HASZN??LATA (30HP)", "ELIX??R HASZN??LATA (MAXHP)"]
UI.battle2 = ["T??MAD??S", "GY??GYITAL HASZN??LATA (30HP)", "ELIX??R HASZN??LATA (MAXHP)"]
UI.equipment = ["FEGYVER", "V??RT", "SISAK", "CIP??", "TALIZM??N", "KIL??P??S"]
UI.equipment2 = ["FEGYVER", "V??RT", "SISAK", "CIP??", "TALIZM??N", "KIL??P??S"]