import variables2
from items import *

class Character:

    def __init__(self, pos_x, pos_y, name, attack, HP, HPMAX, defense, gold, potion, elixir, weapon, armor, helmet, boots, talisman, weaponbag, weaponbag2, armorbag, armorbag2, helmetbag, helmetbag2, bootsbag, bootsbag2, talismanbag, talismanbag2):
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

        self.weapon = weapon
        self.armor = armor
        self.helmet = helmet
        self.boots = boots
        self.talisman = talisman

        self.weaponbag = weaponbag
        self.weaponbag2 = weaponbag2
        self.armorbag = armorbag
        self.armorbag2 = armorbag2
        self.helmetbag = helmetbag
        self.helmetbag2 = helmetbag2
        self.bootsbag = bootsbag
        self.bootsbag2 = bootsbag2
        self.talismanbag = talismanbag
        self.talismanbag2 = talismanbag2
    
    def attackplus(self):

        self.attack = 50
        self.defense = 2
        self.HP = 2000

        if self.weapon in weapon.keys():
            self.attack += weapon[self.weapon]["attack"]

        if self.armor in armor.keys():
            self.defense += armor[self.armor]["armor"]

        if self.helmet in helmet.keys():
            self.HP += helmet[self.helmet]["HP"]

        if self.boots in boots.keys():
            self.HP += boots[self.boots]["HP"]

        if self.talisman in talisman.keys():
            self.attack += talisman[self.talisman]["attack"]
            self.defense += talisman[self.talisman]["armor"]
            self.HP += talisman[self.talisman]["HP"]
    
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
Character.HPMAX = 5000
Character.gold = 50
Character.potion = 3
Character.elixir = 1

Character.weapon = "Zsidó Kés"
Character.armor = "Zsidó Ing"
Character.helmet = "Zsidó Kalap"
Character.boots = "Zsidó Papucs"
Character.talisman = "Zsidó Talizmán"

Character.weaponbag = ["Zsidó Kés", "Geci Szurony"]
Character.weaponbag2 = ["Zsidó Kés", "Geci Szurony"]
Character.armorbag = ["Zsidó Ing", "Geci Vért"]
Character.armorbag2 = ["Zsidó Ing", "Geci Vért"]
Character.helmetbag = ["Zsidó Kalap"]
Character.helmetbag2 = ["Zsidó Kalap"]
Character.bootsbag = ["Zsidó Papucs"]
Character.bootsbag2 = ["Zsidó Papucs"]
Character.talismanbag = ["Zsidó Talizmán"]
Character.talismanbag2 = ["Zsidó Talizmán"]

Character.attackplus(Character)