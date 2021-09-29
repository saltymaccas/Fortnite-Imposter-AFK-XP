import pyautogui as gui
import time

def click(button):
    gui.moveTo(gui.locateOnScreen(button, confidence=0.8))
    gui.mouseDown()
    time.sleep(1)
    gui.mouseUp()


while True:
    gui.moveTo(10,10)
    if gui.locateOnScreen('play.png', confidence=0.8) != None:
        click('play.png')
    
    gui.keyDown('e')
    time.sleep(3)
    gui.keyUp('e')

    gui.keyDown('w')
    time.sleep(3)
    gui.keyUp('w')

    gui.keyDown('a')
    time.sleep(3)
    gui.keyUp('a')
    
    gui.keyDown('s')
    time.sleep(3)
    gui.keyUp('s')

    gui.keyDown('d')
    time.sleep(3)
    gui.keyUp('d')

    gui.keyDown('b')
    time.sleep(3)
    gui.keyUp('b')



    gui.keyDown('f')
    time.sleep(3)
    gui.keyUp('f')

    if gui.locateOnScreen('claim.png', confidence=0.8) != None:
        click('claim.png')
    if gui.locateOnScreen('close.png', confidence=0.8) != None:
        click('close.png')
    if gui.locateOnScreen('continue.png', confidence=0.8) != None:
        click('continue.png')
    if gui.locateOnScreen('three.png', confidence=0.8) != None:
        click('three.png')
    if gui.locateOnScreen('submit.png', confidence=0.8) != None:
        click('submit.png')
