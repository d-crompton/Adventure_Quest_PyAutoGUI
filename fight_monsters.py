import pyautogui # Requires the installation of pillow
import time
import random

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
    # SET-UP CHARACTER
    battle.change_weapon()
    # ADD CONDITION TO CHECK IF YOU'RE ACTUALLY IN BATTLE before starting loop - Enemy health bar?
    while True:
        try: # Check if battle is won
            doneButton = pyautogui.locateOnScreen(battleDoneImage, grayscale=True, confidence=0.8)
            if doneButton != None:
                print("You Won!")
                time.sleep(2)
                leftClick(doneButton.left + (doneButton.width/2), doneButton.top + (doneButton.height/2))
                # TO DO - CHECK HERE IF YOU'VE LEVELLED UP - Window appears after you've "done" the fight
                # NEED TO TEST
                # if(pyautogui.pixel(battle.levelUpE)[0]) == battle.levelUpERed:
                #     print("LEVEL UP")
                break
        except:
            # FAILURE
            if(pyautogui.pixel(battle.failureL[0], battle.failureL[1])[0]) == battle.failureLRed:
                print("You Died!")
                # Click Next button
                time.sleep(2) # CONFIRM THIS IS ENOUGH TIME
                pyautogui.leftClick(battle.failureNextButton[0], battle.failureNextButton[1])
                time.sleep(5) # Wait for Boatman to row across
                # Click whilst avoiding the Hourglass 3 times to return to town
                for i in range(3):
                    xPos = random.randint(battle.boatmanCoords['leftX'], battle.boatmanCoords['rightX'])
                    yPos = random.randint(battle.boatmanCoords['topY'], battle.boatmanCoords['bottomY'])
                    pyautogui.leftClick(xPos, yPos)
                    time.sleep(1)
                break # Break the Battle loop
            else:
            # POTION - If player has low health and more than 0 potions
                if(pyautogui.pixel(battle.healthbar[0], battle.healthbar[1])[0]) == battle.healthbarBlack and numHpPots > 0:
                    pyautogui.leftClick(battle.itemButton[0], battle.itemButton[1])
                    time.sleep(1)
                    leftClick(battle.hpPotionButton[0], battle.hpPotionButton[1])
                    numHpPots =- 1
            # ATTACK
                else:
                    battle.attack()
                    # leftClick(battle.attackButton[0], battle.attackButton[1])
                    # time.sleep(4 + random.randint(1, 3))





