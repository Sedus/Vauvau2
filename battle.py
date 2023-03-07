import variables2
from ui import *
from map import *
from enemy import *

def spawnenemychance():
    Enemy.selected_enemy = enemy_select(Orc(), Goblin(), Slime())
    UI.switchstate("battle")

def attack():
    if Enemy.selected_enemy.HP <= Character.attack:
        variables2.loglist.clear()
        Character.HP -= Enemy.selected_enemy.attack
        loot()
    else:
        Enemy.selected_enemy.HP -= Character.attack
        Character.HP -= Enemy.selected_enemy.attack
        variables2.loglist.insert(0, Character.name + " " + str(Character.attack) + " sebzést okozott " + Enemy.selected_enemy.name + "-nak.")
        variables2.loglist.insert(0, Enemy.selected_enemy.name + " " + str(Enemy.selected_enemy.attack) + " sebzést okozott " + Character.name + "-nak.")
        if Character.HP <= 0:
            os.system("cls")
            cprint (Enemy.selected_enemy.name + " legyőzte " + Character.name + "...", "red")
            cprint("VÉGE", "red")
            input("> ")
            quit()

def loot():
    variables2.loglist.insert(0, Character.name + " legyőzte " + (Enemy.selected_enemy.name + "-ot!"))
    variables2.loglist.insert(0, "Találtál " + str(Enemy.selected_enemy.gold) + " aranyat!")
    Character.gold += Enemy.selected_enemy.gold
    random_item_gen()
    UI.switchstate("play")

def random_item_gen():
    a = random.choice(list(weapon.keys()) + list(armor.keys()) + list(helmet.keys()) + list(boots.keys()) + list(talisman.keys()))
    if a not in (Character.weaponbag + Character.armorbag + Character.helmetbag + Character.bootsbag + Character.talismanbag):
        if a in weapon.keys():
            Character.weaponbag.insert(0, a)
            Character.weaponbag2.insert(0, a)
        if a in armor.keys():
            Character.armorbag.insert(0, a)
            Character.armorbag2.insert(0, a)
        if a in helmet.keys():
            Character.helmetbag.insert(0, a)
            Character.helmetbag2.insert(0, a)
        if a in boots.keys():
            Character.bootsbag.insert(0, a)
            Character.bootsbag2.insert(0, a)
        if a in talisman.keys():
            Character.talismanbag.insert(0, a)
            Character.talismanbag2.insert(0, a)