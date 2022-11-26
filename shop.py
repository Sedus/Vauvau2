from character import *
import variables2

def weaponupgrade():
    if Character.gold >= 10:
        Character.attack += 2
        Character.gold -= 10
        variables2.loglist.insert(0, "Sikeresen fejlesztetted a fegyvered!")
    else:
        variables2.loglist.insert(0, "Nincs elég aranyad!")

def potbuy():
    if Character.gold >= 5:
        Character.potion += 1
        Character.gold -= 5
        variables2.loglist.insert(0, "Vettél egy gyógyitalt!")
    else:
        variables2.loglist.insert(0, "Nincs elég aranyad!")

def elixbuy():
    if Character.gold >= 20:
        Character.elixir += 1
        Character.gold -= 20
        variables2.loglist.insert(0, "Vettél egy elixírt!")
    else:
        variables2.loglist.insert(0, "Nincs elég aranyad!")