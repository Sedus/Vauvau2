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
    
    def stat_calc(self, base_attack = 50, base_defense = 2, base_HP = 2000):
        self.defense =  base_defense + armor[self.armor]["armor"] + talisman[self.talisman]["armor"]
        self.HP = base_HP + helmet[self.helmet]["HP"] + boots[self.boots]["HP"] + talisman[self.talisman]["HP"]
        self.attack = base_attack + weapon[self.weapon]["attack"] + talisman[self.talisman]["attack"]
    
    def heal(self, amount):
        self.HP += amount
        variables2.loglist.insert(0, f"{self.name} élete fel lett töltve {self.HP}-re!")

    def use_potion(self):
        if self.potion > 0:
            self.potion -= 1
            if self.HP + 30 > self.HPMAX:
                self.heal(self, self.HPMAX - self.HP)
            else:
                self.heal(self, 30)
        else:
            variables2.loglist.insert(0, "Nincs gyógyitalod!")

    def use_elixir(self):
        if self.elixir > 0:
            self.elixir -= 1
            self.heal(self, self.HPMAX - self.HP)
        else:
            variables2.loglist.insert(0, "Nincs elixíred!")
        
    def save():
        data = [
            str(Character.pos_x),
            str(Character.pos_y),
            Character.name,
            str(Character.HPMAX),
            str(Character.gold),
            str(Character.potion),
            str(Character.elixir),
            Character.weapon,
            Character.armor,
            Character.helmet,
            Character.boots,
            Character.talisman
        ]

        with open("save.txt", "w", encoding='utf-8') as f:
            f.write("\n".join(data))
    
    def load():
        with open("save.txt", "r", encoding='utf-8') as f:
            load_list = [line.strip() for line in f.readlines()]

        Character.pos_x = int(load_list[0])
        Character.pos_y = int(load_list[1])
        Character.name = load_list[2]
        Character.HPMAX = int(load_list[3])
        Character.gold = int(load_list[4])
        Character.potion = int(load_list[5])
        Character.elixir = int(load_list[6])
        Character.weapon = load_list[7]
        Character.armor = load_list[8]
        Character.helmet = load_list[9]
        Character.boots = load_list[10]
        Character.talisman = load_list[11]

        variables2.loglist.insert(0, "Bejelentkeztél " + Character.name + " felhasználóval!")


Character.pos_x = 0
Character.pos_y = 0
Character.name = "Gecisfasz"
Character.HPMAX = 5000
Character.gold = 50
Character.potion = 3
Character.elixir = 1

Character.weapon = "Fa Kard"
Character.armor = "Rongyos Bőrvért"
Character.helmet = "Bőr Kalap"
Character.boots = "Bőr Lépő"
Character.talisman = "Védelmező Talizmán"

Character.weaponbag = ["Fa Kard", "Fém Penge", "Sárkánycsont Kard", "Csillagfény Kard", "Kozmikus Fénykard", "Időkerék Kardja"]
Character.weaponbag2 = ["Fa Kard", "Fém Penge", "Sárkánycsont Kard", "Csillagfény Kard", "Kozmikus Fénykard", "Időkerék Kardja"]
Character.armorbag = ["Rongyos Bőrvért", "Fém Láncpáncél", "Sárkánycsont Lemezpáncél", "Viharégette Harci Páncél", "Ősi Sárkánybőr Vértezet", "Főnix Kardvértezet"]
Character.armorbag2 = ["Rongyos Bőrvért", "Fém Láncpáncél", "Sárkánycsont Lemezpáncél", "Viharégette Harci Páncél", "Ősi Sárkánybőr Vértezet", "Főnix Kardvértezet"]
Character.helmetbag = ["Bőr Kalap", "Fém Sisak", "Sárkánycsont Sisak", "Viharégette Páncélsisak", "Ősi Sárkánybőr Sisak", "Főnix Korona"]
Character.helmetbag2 = ["Bőr Kalap", "Fém Sisak", "Sárkánycsont Sisak", "Viharégette Páncélsisak", "Ősi Sárkánybőr Sisak", "Főnix Korona"]
Character.bootsbag = ["Bőr Lépő", "Fém Bakancs", "Sárkánycsont Cipő", "Viharégette Lábbeli", "Ősi Sárkánybőr Csizma", "Főnix Cipő"]
Character.bootsbag2 = ["Bőr Lépő", "Fém Bakancs", "Sárkánycsont Cipő", "Viharégette Lábbeli", "Ősi Sárkánybőr Csizma", "Főnix Cipő"]
Character.talismanbag = ["Védelmező Talizmán", "Holdfény Talizmán", "Rejtélyes Talizmán", "Kozmikus Talizmán", "Karmazsin Talizmán", "Időtlen Talizmán"]
Character.talismanbag2 = ["Védelmező Talizmán", "Holdfény Talizmán", "Rejtélyes Talizmán", "Kozmikus Talizmán", "Karmazsin Talizmán", "Időtlen Talizmán"]