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
        elif hova == "play":
            Character.stat_calc(Character)
            UI.counter = 0
            UI.state = hova
            UI.play = UI.play2.copy()
            os.system("cls")
            UI.print_map(Map.map2)
            UI.menu_layout2()
            UI.play[UI.counter] = "> " + UI.play[UI.counter] + " <"
            UI.navmenuprint(UI.play)
        elif hova == "shop":
            UI.counter = 0
            UI.state = hova
            UI.shop = UI.shop2.copy()
            os.system("cls")
            UI.shoplayout()
            UI.shop[UI.counter] = "> " + UI.shop[UI.counter] + " <"
            UI.navmenuprint(UI.shop)
        elif hova == "battle":
            UI.counter = 0
            UI.state = hova
            UI.battle = UI.battle2.copy()
            variables2.loglist.clear()
            os.system("cls")
            UI.battlelayout()
            UI.battle[UI.counter] = "> " + UI.battle[UI.counter] + " <"
            UI.navmenuprint(UI.battle)
        elif hova == "equipment":
            UI.counter = 0
            UI.state = hova
            UI.equipment = UI.equipment2.copy()
            variables2.loglist.clear()
            os.system("cls")
            UI.equipmentlayout()
            UI.equipment[UI.counter] = "> " + UI.equipment[UI.counter] + " <"
            UI.navmenuprint(UI.equipment)
        elif hova == "inequipment":
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
                Character.weaponbag = Character.weaponbag2.copy()
                Character.weaponbag[UI.counter] = "> " + Character.weaponbag[UI.counter] + " <"
                UI.navmenuprint(Character.weaponbag)
            elif variables2.equipment_type == "armor":
                Character.armorbag = Character.armorbag2.copy()
                Character.armorbag[UI.counter] = "> " + Character.armorbag[UI.counter] + " <"
                UI.navmenuprint(Character.armorbag)
            elif variables2.equipment_type == "helmet":
                Character.helmetbag = Character.helmetbag2.copy()
                Character.helmetbag[UI.counter] = "> " + Character.helmetbag[UI.counter] + " <"
                UI.navmenuprint(Character.helmetbag)
            elif variables2.equipment_type == "boots":
                Character.bootsbag = Character.bootsbag2.copy()
                Character.bootsbag[UI.counter] = "> " + Character.bootsbag[UI.counter] + " <"
                UI.navmenuprint(Character.bootsbag)
            elif variables2.equipment_type == "talisman":
                Character.talismanbag = Character.talismanbag2.copy()
                Character.talismanbag[UI.counter] = "> " + Character.talismanbag[UI.counter] + " <"
                UI.navmenuprint(Character.talismanbag)


    def navigate(list1, list2, direction):
        list1[UI.counter] = list2[UI.counter]
        UI.counter = (UI.counter + direction) % len(list1)
        list1[UI.counter] = "> " + list1[UI.counter] + " <"

    def menu_layout2():
        UI.draw()
        cprint("JELENLEGI POZÍCIÓ: " + Map.biom[Map.map[Character.pos_y][Character.pos_x]]["name"], "green", attrs=["bold"])
        UI.draw()
        cprint("NÉV:", "green", attrs=["bold"], end=" ")
        cprint("{: <45}".format(str(Character.name)), "blue", attrs=["bold"], end=" ")
        cprint("FEGYVER:", "green", attrs=["bold"], end=" ")
        UI.print_colored_text(str(Character.weapon + "\n"), weapon[Character.weapon]["rarity"])

        cprint("ÉLET:", "green", attrs=["bold"], end=" ")
        cprint("{: <44}".format(str(Character.HP) + "/" + str(Character.HPMAX)), "red", end=" ")
        cprint("VÉRT:", "green", attrs=["bold"], end=" ")
        UI.print_colored_text(str(Character.armor + "\n"), armor[Character.armor]["rarity"])

        cprint("SEBZÉS:", "green", attrs=["bold"], end=" ")
        cprint("{: <42}".format(str(Character.attack)), "red", end=" ")
        cprint("SIAK:", "green", attrs=["bold"], end=" ")
        UI.print_colored_text(str(Character.helmet + "\n"), helmet[Character.helmet]["rarity"])

        cprint("PÁNCÉL:", "green", attrs=["bold"], end=" ")
        cprint("{: <42}".format(str(Character.defense)), "blue", attrs=["bold"], end=" ")
        cprint("CIPŐ:", "green", attrs=["bold"], end=" ")
        UI.print_colored_text(str(Character.boots + "\n"), boots[Character.boots]["rarity"])

        cprint("GYÓGYITAL:", "green", attrs=["bold"], end=" ")
        cprint("{: <39}".format(str(Character.potion) + " darab"), "red", end=" ")
        cprint("TALIZMÁN:", "green", attrs=["bold"], end=" ")
        UI.print_colored_text(str(Character.talisman + "\n"), talisman[Character.talisman]["rarity"])

        cprint("ELIXÍR:", "green", attrs=["bold"], end=" ")
        cprint("{: <39}".format(str(Character.elixir) + " darab"), "cyan", attrs=["bold"])
        cprint("ARANY:", "green", attrs=["bold"], end=" ")
        cprint(str(Character.gold) + "$", "yellow", attrs=["bold"])

    def shoplayout():
        UI.draw()

        items = {
            "NÉV:": (Character.name, "blue"),
            "ÉLET:": (str(Character.HP) + "/" + str(Character.HPMAX), "red"),
            "SEBZÉS:": (str(Character.attack), "red"),
            "PÁNCÉL:": (str(Character.defense), "blue"),
            "GYÓGYITAL:": (str(Character.potion) + " darab", "red"),
            "ELIXÍR:": (str(Character.elixir) + " darab", "cyan"),
            "ARANY:": (str(Character.gold) + "$", "yellow")
        }

        for item, (value, color) in items.items():
            cprint(f"{item} ", "green", attrs=["bold"], end="")
            cprint(value, color, attrs=["bold"])

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
        UI.draw()

        items = {
            "FEGYVER": (Character.weapon, weapon),
            "VÉRT": (Character.armor, armor),
            "SISAK": (Character.helmet, helmet),
            "CIPŐ": (Character.boots, boots),
            "TALIZMÁN": (Character.talisman, talisman)
        }

        for item, (character_item, item_dict) in items.items():
            cprint(f"{item}:", "green", attrs=["bold"], end=" ")
            UI.print_colored_text(str(character_item + "\n"), item_dict[character_item]["rarity"])

    def print_colored_text(text, rarity):
        if isinstance(rarity, tuple):
            for char in text:
                color = random.choice(rarity)
                if (color == "red" or color == "blue"):
                    cprint(char, color, end="")
                else:
                    cprint(char, color, attrs=["bold"], end="")
        else:
            color = rarity
            if (color == "red" or color == "blue"):
                cprint(text, color, end="")
            else:
                cprint(text, color, attrs=["bold"], end="")

    def inequipmentlayout():
        equipment_type = variables2.equipment_type
        counter = UI.counter

        if equipment_type == "weapon":
            rarity = weapon[Character.weaponbag2[counter]]["rarity"]
            UI.print_colored_text(UI.weaponstring, rarity)
            cprint("\nFelszerelt tárgy:                                 Kiválasztott tárgy:", "green", attrs=["bold"])
            UI.print_colored_text(f"  -{Character.weapon} {' ' * (46 - len(Character.weapon))}  -{Character.weaponbag2[counter]}\n", rarity)
            UI.print_colored_text(f"    -SEBZÉS: {str(weapon[Character.weapon]['attack'])} {' ' * (37 - len(str(weapon[Character.weapon]['attack'])))}    -SEBZÉS: {str(weapon[Character.weaponbag2[counter]]['attack'])}\n", rarity)
        elif equipment_type == "armor":
            rarity = armor[Character.armorbag2[counter]]["rarity"]
            UI.print_colored_text(UI.armorstring, rarity)
            cprint("\nFelszerelt tárgy:                                 Kiválasztott tárgy:", "green", attrs=["bold"])
            UI.print_colored_text(f"  -{Character.armor} {' ' * (46 - len(Character.armor))}  -{Character.armorbag2[counter]}\n", rarity)
            UI.print_colored_text(f"    -PÁNCÉL: {str(armor[Character.armor]['armor'])} {' ' * (37 - len(str(armor[Character.armor]['armor'])))}    -PÁNCÉL: {str(armor[Character.armorbag2[counter]]['armor'])}\n", rarity)
        elif equipment_type == "helmet":
            rarity = helmet[Character.helmetbag2[counter]]["rarity"]
            UI.print_colored_text(UI.helmetstring, rarity)
            cprint("\nFelszerelt tárgy:                                 Kiválasztott tárgy:", "green", attrs=["bold"])
            UI.print_colored_text(f"  -{Character.helmet} {' ' * (46 - len(Character.helmet))}  -{Character.helmetbag2[counter]}\n", rarity)
            UI.print_colored_text(f"    -HP: {str(helmet[Character.helmet]['HP'])} {' ' * (41 - len(str(helmet[Character.helmet]['HP'])))}    -HP: {str(helmet[Character.helmetbag2[counter]]['HP'])}\n", rarity)
        elif equipment_type == "boots":
            rarity = boots[Character.bootsbag2[counter]]["rarity"]
            UI.print_colored_text(UI.bootsstring, rarity)
            cprint("\nFelszerelt tárgy:                                 Kiválasztott tárgy:", "green", attrs=["bold"])
            UI.print_colored_text(f"  -{Character.boots} {' ' * (46 - len(Character.boots))}  -{Character.bootsbag2[counter]}\n", rarity)
            UI.print_colored_text(f"    -HP: {str(boots[Character.boots]['HP'])} {' ' * (41 - len(str(boots[Character.boots]['HP'])))}    -HP: {str(boots[Character.bootsbag2[counter]]['HP'])}\n", rarity)
        elif equipment_type == "talisman":
            rarity = talisman[Character.talismanbag2[counter]]["rarity"]
            UI.print_colored_text(UI.talismanstring, rarity)
            cprint("\nFelszerelt tárgy:                                 Kiválasztott tárgy:", "green", attrs=["bold"])
            UI.print_colored_text(f"  -{Character.talisman} {' ' * (46 - len(Character.talisman))}  -{Character.talismanbag2[counter]}\n", rarity)
            UI.print_colored_text(f"    -SEBZÉS: {str(talisman[Character.talisman]['attack'])} {' ' * (37 - len(str(talisman[Character.talisman]['attack'])))}    -SEBZÉS: {str(talisman[Character.talismanbag2[counter]]['attack'])}\n", rarity)
            UI.print_colored_text(f"    -PÁNCÉL: {str(talisman[Character.talisman]['armor'])} {' ' * (37 - len(str(talisman[Character.talisman]['armor'])))}    -PÁNCÉL: {str(talisman[Character.talismanbag2[counter]]['armor'])}\n", rarity)
            UI.print_colored_text(f"    -HP: {str(talisman[Character.talisman]['HP'])} {' ' * (41 - len(str(talisman[Character.talisman]['HP'])))}    -HP: {str(talisman[Character.talismanbag2[counter]]['HP'])}\n", rarity)

    def inequipmentup(list1, list2):
        os.system("cls")
        UI.navigate(list1, list2, -1)
        UI.inequipmentlayout()
        UI.navmenuprint(list1)
    
    def inequipmentdown(list1, list2):
        os.system("cls")
        UI.navigate(list1, list2, 1)
        UI.inequipmentlayout()
        UI.navmenuprint(list1)

    def draw():
        cprint("=" * 78, "red")

    def logprint():
        print("\n\n\n\n\n\n\n\n\n")
        cprint("LEGUTÓBBI ESEMÉNYEK:", "green", attrs=["bold"])
        for result in variables2.loglist:
            cprint("    " + str(result), "magenta", attrs=["bold"])
    
    def navmenuprint(lst):
        UI.draw()
        for i in lst:
            color = "white" if i == lst[UI.counter] else "green"
            bg_color = "on_magenta" if i == lst[UI.counter] else None
            attrs = ["bold"]
            cprint(i, color, bg_color, attrs=attrs)
        UI.draw()
        UI.logprint()

    def start():
        tprint("vauvau    2", "tarty1")
        tprint("PRE-ALPHA    0.6.0", "tarty1")
        cprint("NYOMJ MEG BÁRMIT AZ INDULÁSHOZ!", "green", attrs=["bold"])
        input (">")
        UI.switchstate("menu")

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

    weaponstring = ("""
._._._._._._._._._|__________________________________________________________
|_|_|_|_|_|_|_|_|_|_________________________________________________________/
                  |
    """)

    armorstring = ("""
                     _________________________ 
                    |<><><>     |  |    <><><>|
                    |<>         |  |        <>|
                    |           |  |          |
                    |  (______ <\-/> ______)  |
                    |  /_.-=-.\| " |/.-=-._\  | 
                    |   /_    \(o_o)/    _\   |
                    |    /_  /\/ ^ \/\  _\    |
                    |      \/ | / \ | \/      |
                    |_______ /((( )))\ _______|
                    |      __\ \___/ /__      |
                    |--- (((---'   '---))) ---|
                    |           |  |          |
                    |           |  |          |
                    :           |  |          :     
                     \<>        |  |       <>/      
                      \<>       |  |      <>/       
                       \<>      |  |     <>/       
                        `\<>    |  |   <>/'         
                          `\<>  |  |  <>/'         
                            `\<>|  |<>/'         
                              `-.  .-`           
                                '--'
    """)

    helmetstring = ("""                                                   
                                _
                                ,''/., _
                        `.-._\`/. ( //'/'`.
                    _.-`-. ``' ` `(   -. \\
                    ,'  ,    ,-:._ _..-.. \/
                / ,'/ ,`.( _.'-'.     )/
                `.\ '(   ,'      `.
                    `._\ /'       \ \\
                        /:         \ \-.
                        ,;':._______...-'_)
                        \:/-.._______..-_|
                        : :\   `----'|'-;
                        \ :\    : : ;:/
                        \ ``.   ; /;/
                            )   `.  /,'
                        ,'      `-' \\
                        /  .--.       )
                        /_.---._`._   /
                                `.__.'
    """)

    bootsstring = ("""
                            ________
                        __(_____  <|
                        (____ / <| <|
                        (___ /  <| L`-------.
                        (__ /   L`--------.  \\
                        /  `.    ^^^^^ |   \  |
                        |     \---------'    |/
                        |______|____________/]
                        [_____|`-.__________]
    """)

    talismanstring = ("""
                             _______________
                            |@@@@|     |####|
                            |@@@@|     |####|
                            |@@@@|     |####|
                            \@@@@|     |####/
                             \@@@|     |###/
                              `@@|_____|##'
                                   (O)
                                .-'''''-.
                              .'  * * *  `.
                             :  *       *  :
                            : ~           ~ :
                            : ~           ~ :
                             :  *       *  :
                              '.  * * *  .'
                                '-.....-'
    """)

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