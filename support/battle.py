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
    # but the actual weapon is the monster's weakness
    'Fire': 476, # Guardian Spear - No ice weapon on char
    'Water': 517, # Energy weapon
    'Wind': 552, # Earth weapon
    'Ice': 588, # Fire weapon
    'Earth': 623, # Wind weapon
    'Energy': 655, # Water weapon
    'Light': 692, # Darkness weapon
    'Darkness': 727 # Light weapon
}
shieldsButton = (963, 631)
guardianShield = (1329, 492)
petsButton = (964, 716)
petsXCoord = 1327
petsYCoord = {
    'Fire': 525, # Ice pet
    'Water': 552, # Energy pet
    'Wind': 0, # No earth pets
    'Ice': 585, # Fire pet
    'Earth': 619, # Wind pet
    'Energy': 650, # Water pet
    'Light': 687, # Darkness pet
    'Darkness': 718 # Light pet
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
def change_equipment():
    pyautogui.moveTo(enemyPic[0], enemyPic[1])
    time.sleep(2)

    elemNames = ['Fire', 'Water', 'Wind', 'Ice', 'Earth', 'Energy', 'Light', 'Darkness']

    for i in range(8):
        image = f'./images/elements/{i}.png'
        try:
            elementOnScreen = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9)
            if elementOnScreen != None:
                # Select Weapon
                pyautogui.leftClick(weaponsButton[0], weaponsButton[1])
                time.sleep(1)
                pyautogui.doubleClick(weaponsXCoord, weaponsYCoords[elemNames[i]], 2)
                # Select Pet - If Wind monster then ignore because no Earth pet just keep current pet
                if elemNames[i] != 'Wind':
                    pyautogui.leftClick(petsButton[0], petsButton[1])
                    time.sleep(1)
                    pyautogui.doubleClick(petsXCoord, petsYCoord[elemNames[i]], 2)
                break  
        except:
            continue

def equip_guardian_shield():
    time.sleep(1)
    leftClick(shieldsButton[0], shieldsButton[1])
    time.sleep(1)
    pyautogui.doubleClick(guardianShield[0], guardianShield[1])

def death_sequence():
    print("You Died!")
    time.sleep(2)
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