class Enemy:

    def __init__(self, name, attack, HP, defense):
        self.name = name
        self.attack = attack
        self.HP = HP
        self.defense = defense

    def get_attack(self):
        
        attack = self.attack
        return attack

    def get_defense(self):

        return self.defense

    def get_HP(self):

        HP = self.HP
        return HP


Enemy.attack = 1
Enemy.name = "llllllllllllllllll"
Enemy.HP = 1