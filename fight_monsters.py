import pyautogui # Requires the installation of pillow
import time

import support.town as town
import support.battle as battle
from support.supportFunctions import leftClick

# VARIABLES
numBattles = 0
numHpPots = 2
battleDoneImage = './images/battle_done.png'

# SCRIPT
time.sleep(5) # For user to switch to AQ window

while True:
# In Town
    if(pyautogui.pixel(town.todaysEventButton[0], town.todaysEventButton[1])[0]) == town.todaysEventButtonRed:
        if numBattles > 0:
            leftClick(town.healingFountain[0], town.healingFountain[1])
            numHpPots = town.refill_hp_potions(numHpPots)
            time.sleep(1)
        leftClick(town.startBattle[0], town.startBattle[1])
        numBattles += 1
        print(f"Starting Battle {numBattles}...")
        time.sleep(5)

# In Battle
    battle.change_equipment()
    if numBattles < 2:
        battle.equip_guardian_shield()

    while True:
        try: # Check if battle is won
            doneButton = pyautogui.locateOnScreen(battleDoneImage, grayscale=True, confidence=0.8)
            if doneButton != None:
                time.sleep(2)
                leftClick(doneButton.left + (doneButton.width/2), doneButton.top + (doneButton.height/2))
                # TODO - Check if you've levelled up and then click the "Next" button after Level up animation 
                # time.sleep(2) # Wait for level up animation
                break
        except:
            # FAILURE
            if(pyautogui.pixel(battle.failureL[0], battle.failureL[1])[0]) == battle.failureLRed:
                battle.death_sequence()
                break
            else:
            # POTION - If player has low health and more than 0 potions
                if(pyautogui.pixel(battle.healthbar[0], battle.healthbar[1])[0]) == battle.healthbarBlack and numHpPots > 0:
                    numHpPots = battle.drink_health_potion(numHpPots)
            # ATTACK
                else:
                    battle.attack()





