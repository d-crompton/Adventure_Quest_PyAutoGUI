import pyautogui
import time

# Co-ordinates
failureL = (923, 445)
failureNextButton = (957, 577)
boatmanCoords = {
                    'leftX': 1130,
                    'rightX': 1580,
                    'topY': 50,
                    'bottomY': 500
                }
attackButton = (957, 319)
healthbar = (674, 862)
itemButton = (959, 548)
hpPotionButton = (1216, 460)
weaponsButton = (960, 588)
weaponsXCoord = 1334 # The middle of all the buttons in the weapons' sub-menu
weaponsYCoords = { # The Y positions of each button in the sub-menu, their names are the monster's element
    'Fire': 476, # Guardian Spear - No ice weapon on char X
    'Water': 517, # Energy weapon
    'Wind': 552, # Earth weapon X
    'Ice': 588, # Fire weapon X
    'Earth': 623, # Wind weapon X
    'Energy': 655, # Water weapon X
    'Light': 692, # Darkness weapon X
    'Darkness': 727 # Light weapon X
}
enemyPic = (1479, 888)

# Colour Values
failureLRed = 123
healthbarBlack = 10

# Functions
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