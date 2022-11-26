from character import *

class Map:
    def __init__(self, map, map2, len_x, len_y, tiles, biom):
        self.map = map
        self.map2 = map2
        self.len_x = len_x
        self.len_y = len_y
        self.tiles = tiles
        self.biom = biom

    def createmap():
        for number5 in range(5):
            innerlist = []
            for number7 in range(7):
                #abc = listToString(random.choices(Map.tiles))
                #abc = "bolt"
                abc = "erdő"
                innerlist.append(abc)
            Map.map.append(innerlist)
        Map.len_y = len(Map.map)-1
        Map.len_x = len(Map.map[0])-1
        Map.map2[Character.pos_y][Character.pos_x] = "X"

Map.len_x = 0
Map.len_y = 0
Map.tiles = ["síkság", "erdő", "híd", "hegység", "bolt", "béla", "küldetés"]
Map.map = []
Map.map2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
Map.biom = {
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