# Testing if code can identify the elements
import pyautogui
import time
import support.battle as battle

time.sleep(5) # Time to switch to game

pyautogui.moveTo(battle.enemyPic[0], battle.enemyPic[1])
time.sleep(2)

elemNames = ['Fire', 'Water', 'Wind', 'Ice', 'Earth', 'Energy', 'Light', 'Darkness']

for i in range(8):
    image = f'./images/elements/{i}.png'
    try:
        elementOnScreen = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9)
        if elementOnScreen != None:
            print(f'Monster is {elemNames[i]}')  
            pyautogui.leftClick(battle.weaponsButton[0], battle.weaponsButton[1])
            time.sleep(1)
            pyautogui.doubleClick(battle.weaponsXCoord, battle.weaponsYCoords[elemNames[i]], 2)
            break  
    except:
        continue