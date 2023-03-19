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
    variables2.loglist.insert(1, "Találtál " + str(Enemy.selected_enemy.gold) + " aranyat!")
    variables2.loglist.insert(2, "Találtál egy tárgyat: " + random_item_gen())
    Character.gold += Enemy.selected_enemy.gold
    UI.switchstate("play")

def random_item_gen():
    a = random.choice(list(weapon.keys()) + list(armor.keys()) + list(helmet.keys()) + list(boots.keys()) + list(talisman.keys()))
    if a not in (Character.weaponbag + Character.armorbag + Character.helmetbag + Character.bootsbag + Character.talismanbag):
        if a in weapon.keys():
            Character.weaponbag.extend(a)
            Character.weaponbag2.extend(a)
        if a in armor.keys():
            Character.armorbag.extend(a)
            Character.armorbag2.extend(a)
        if a in helmet.keys():
            Character.helmetbag.extend(a)
            Character.helmetbag2.extend(a)
        if a in boots.keys():
            Character.bootsbag.extend(a)
            Character.bootsbag2.extend(a)
        if a in talisman.keys():
            Character.talismanbag.extend(a)
            Character.talismanbag2.extend(a)
    return a