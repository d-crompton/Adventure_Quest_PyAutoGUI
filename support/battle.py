import pyautogui
import time
import random

from support.supportFunctions import leftClick

# Co-ordinates
attackButton = (957, 319)
healthbar = (674, 862)
itemButton = (959, 548)
hpPotionButton = (1216, 460)
weaponsButton = (960, 588)
weaponsXCoord = 1334 # The middle of all the buttons in the weapons' sub-menu
weaponsYCoords = { # The Y positions of each button in the sub-menu, their names are the monster's element
    'Fire': 476, # Guardian Spear - No ice weapon on char
    'Water': 517, # Energy weapon
    'Wind': 552, # Earth weapon
    'Ice': 588, # Fire weapon
    'Earth': 623, # Wind weapon
    'Energy': 655, # Water weapon
    'Light': 692, # Darkness weapon
    'Darkness': 727 # Light weapon
}
enemyPic = (1479, 888)
levelUpE = (884, 282)
failureL = (923, 445)
failureNextButton = (957, 577)
boatmanCoords = {
                    'leftX': 1130,
                    'rightX': 1580,
                    'topY': 50,
                    'bottomY': 500
                }

# Colour Values
levelUpERed = 249
failureLRed = 123
healthbarBlack = 10

# Functions
# TO DO - Add change to Pet and then change function name to change_equipment
def change_weapon():
    pyautogui.moveTo(enemyPic[0], enemyPic[1])
    time.sleep(2)

    elemNames = ['Fire', 'Water', 'Wind', 'Ice', 'Earth', 'Energy', 'Light', 'Darkness']

    for i in range(8):
        image = f'./images/elements/{i}.png'
        try:
            elementOnScreen = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9)
            if elementOnScreen != None:
                pyautogui.leftClick(weaponsButton[0], weaponsButton[1])
                time.sleep(1)
                pyautogui.doubleClick(weaponsXCoord, weaponsYCoords[elemNames[i]], 2)
                break  
        except:
            continue

def death_sequence():
    print("You Died!")
    time.sleep(2) # CONFIRM THIS IS ENOUGH TIME
    pyautogui.leftClick(failureNextButton[0], failureNextButton[1])
    time.sleep(5) # Wait for Boatman to row across
    # Click whilst avoiding the Hourglass 3 times to return to town
    for i in range(3):
        xPos = random.randint(boatmanCoords['leftX'], boatmanCoords['rightX'])
        yPos = random.randint(boatmanCoords['topY'], boatmanCoords['bottomY'])
        pyautogui.leftClick(xPos, yPos)
        time.sleep(1)

def drink_health_potion(numHpPots):
    pyautogui.leftClick(itemButton[0], itemButton[1])
    time.sleep(1)
    leftClick(hpPotionButton[0], hpPotionButton[1])
    numHpPots -= 1
    return numHpPots

def attack():
    leftClick(attackButton[0], attackButton[1])
    time.sleep(4 + random.randint(1, 3))