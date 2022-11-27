import variables2
from ui import *
from map import *
from enemy import *

def spawnenemychance():
    Enemy.selected_enemy = enemy_select(Orc(), Goblin())
    UI.switchstate("battle")

def attack():
    if Enemy.selected_enemy.HP <= Character.attack:
        variables2.loglist.clear()
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
    UI.switchstate("play")