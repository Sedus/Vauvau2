import random

class Enemy:

    def __init__(self, name, attack, HP, HPMAX, defense, gold):
        self.name = name
        self.attack = attack
        self.HP = HP
        self.HPMAX = HPMAX
        self.defense = defense
        self.gold = gold

    selected_enemy = ""

class Orc(Enemy):
    def __init__(self):
        super().__init__(random.choice(list(open("orc_names.txt"))).strip(), 10, 100, 100, 6, 90)

class Goblin(Enemy):
    def __init__(self):
        super().__init__(random.choice(list(open("goblin_names.txt"))).strip(), 10, 111, 111, 1, 9)

class Slime(Enemy):
    def __init__(self):
        super().__init__(random.choice(list(open("slime_names.txt"))).strip(), 5, 222, 222, 1, 4)

def enemy_select(*args):
    enemy_list = [*args]
    length_list = (len(enemy_list))-1
    enemy_chance = random.randint(0, length_list)
    enemy_1 = enemy_list[enemy_chance]
    return enemy_1