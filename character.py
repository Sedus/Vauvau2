class Character:

    def __init__(self, name, attack, HP):
        self.name = name
        self.attack = attack
        self.HP = HP

    def get_attack(self):
        
        attack = self.attack
        return attack

    def get_HP(self):

        HP = self.HP
        return HP


Character.attack = 17
Character.name = "oooooooooop"
Character.HP = 99
