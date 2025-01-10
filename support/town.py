from .supportFunctions import leftClick

# Co-ordinates
todaysEventButton = (532, 632)
healingFountain = (1117, 801)
guardianTower = (1072, 360)
towerDoor = (995, 389)
potionsChest = (1422, 765)
leaveTower = (948, 81) 
startBattle = (1401, 333)

# Colour Values
todaysEventButtonRed = 157

# Functions
def refill_hp_potions(numHpPots):
    if numHpPots < 2:
                leftClick(guardianTower[0], guardianTower[1])
                leftClick(towerDoor[0], towerDoor[1])
                leftClick(potionsChest[0], potionsChest[1])
                numHpPots = 2
                leftClick(leaveTower[0], leaveTower[1])
    return numHpPots


