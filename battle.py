import random
import variables2
from ui import *
from map import *

def spawnenemychance():
    if  Map.biom [Map.map[Character.pos_y][Character.pos_x]] ["spawn_enemy"]:
        if random.randint (1, 10) <= 100:
            variables2.enemy = random.choice(variables2.enemy_list)
            variables2.mobs ["Goblin"] ["name"] = random.choice(variables2.goblin_names)
            variables2.mobs ["Ork"] ["name"] = random.choice(variables2.ork_names)
            variables2.mobs ["Slime"] ["name"] = random.choice(variables2.slime_names)
            variables2.enemy_hp = variables2.mobs [variables2.enemy] ["hp"]
            variables2.enemy_atk = variables2.mobs [variables2.enemy] ["atk"]
            UI.switchstate("battle")

def attack():
    if variables2.enemy_hp <= Character.attack:
        variables2.loglist.clear()
        loot()
    else:
        variables2.enemy_hp -= Character.attack
        Character.HP -= variables2.enemy_atk
        variables2.loglist.insert(0, Character.name + " " + str(Character.attack) + " sebzést okozott " + variables2.mobs [variables2.enemy] ["name"] + "-nak.")
        variables2.loglist.insert(0, variables2.mobs [variables2.enemy] ["name"] + " " + str(variables2.enemy_atk) + " sebzést okozott " + Character.name + "-nak.")
        if Character.HP <= 0:
            os.system("cls")
            cprint (variables2.mobs [variables2.enemy] ["name"] + " legyőzte " + Character.name + "...", "red")
            cprint("VÉGE", "red")
            input("> ")
            quit()

def loot():
    variables2.loglist.insert(0, Character.name + " legyőzte " + (variables2.mobs [variables2.enemy] ["name"] + "-ot!"))
    variables2.loglist.insert(0, "Találtál " + str(variables2.mobs [variables2.enemy] ["gold"]) + " aranyat!")
    Character.gold += variables2.mobs [variables2.enemy] ["gold"]
    UI.switchstate("play")