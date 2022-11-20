from functions2 import listToString

player_hp = 250
player_hpmax = 500
player_atk = 8
pot = 3
elix = 1
gold = 50
x = 0
y = 0
name = "Faszosjózsi"
tiles = ["síkság", "erdő", "híd", "hegység", "bolt", "béla", "küldetés"]
y_len = 0
x_len = 0
enemy = ""
loglist = []
counter = 0

menu = True
play = False
shop = False
battle = False
equipment = False

map = []
map2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
biom = {
    "síkság": {
        "name": "SÍKSÁG",
        "spawn_enemy": True,
        "icon": "♥"},
    "erdő": {
        "name": "ERDŐ",
        "spawn_enemy": True,
        "icon": "♠"},
    "híd": {
        "name": "HÍD",
        "spawn_enemy": True,
        "icon": "♣"},
    "hegység": {
        "name": "HEGYSÉG",
        "spawn_enemy": True,
        "icon": "♦"},
    "bolt": {
        "name": "BOLT",
        "spawn_enemy": False,
        "icon": "$"},
    "béla": {
        "name": "BÉLA",
        "spawn_enemy": True,
        "icon": "¤"},
    "küldetés": {
        "name": "KÜLDETÉS",
        "spawn_enemy": True,
        "icon": "@"},
}

enemy_list = ["Goblin", "Ork", "Slime"]

goblin_names = ["Ogning", "Glact", "Zolb", "Etog"]
ork_names = ["Zilug", "Varbuk", "Zarfu", "Dretkag", "Soughat", "Frikug", "Quimghig", "Orpigig", "Waruk", "Surpigig"]
slime_names = ["Gloop", "Blob", "Bloop"]

enemy_hp = None
enemy_atk = None

mobs = {
    "Goblin": {
        "hp" : 15,
        "atk" : 8,
        "gold" : 8,
        "name" : ""
   },
    "Ork": {
        "hp" : 35,
        "atk" : 10,
        "gold" : 18,
        "name" : ""
   },
    "Slime": {
        "hp" : 30,
        "atk" : 15,
        "gold" : 12,
        "name" : ""
   }
}

list = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]
list2 = ["ÚJ JÁTÉK", "JÁTÉK BETÖLTÉSE", "SZABÁLYOK", "KILÉPÉS"]

list3 = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]
list4 = ["MENTÉS ÉS KILÉPÉS", "▲ FEL", "► JOBBRA", "▼ LE", "◄ BALRA", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)", "FELSZERELÉS", "BELÉPÉS"]

list5 = ["TÁMADÁS", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)"]
list6 = ["TÁMADÁS", "GYÓGYITAL HASZNÁLATA (30HP)", "ELIXÍR HASZNÁLATA (MAXHP)"]

bool1 = True
bool2 = True