import variables2

class Character:

    def __init__(self, pos_x, pos_y, name, attack, HP, HPMAX, defense, gold, potion, elixir):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.name = name
        self.attack = attack
        self.HP = HP
        self.HPMAX = HPMAX
        self.defense = defense
        self.gold = gold
        self.potion = potion
        self.elixir = elixir

    def heal(amount):
        Character.HP += amount
        variables2.loglist.insert(0, Character.name + " élete fel lett töltve " + str(Character.HP) + "-re!")

    def usepotion():
        if Character.potion > 0:
            Character.potion -= 1
            if Character.HP + 30 > Character.HPMAX:
                Character.heal(Character.HPMAX - Character.HP)
            else:
                Character.heal(30)
        else:
            variables2.loglist.insert(0, "Nincs gyógyitalod!")

    def useelixir():
        if Character.elixir > 0:
            Character.elixir -= 1
            Character.heal(Character.HPMAX - Character.HP)
        else:
            variables2.loglist.insert(0, "Nincs elixíred!")

Character.pos_x = 0
Character.pos_y = 0
Character.name = "Gecisfasz"
Character.attack = 90
Character.HP = 2000
Character.HPMAX = 500
Character.defense = 2
Character.gold = 50
Character.potion = 3
Character.elixir = 1
