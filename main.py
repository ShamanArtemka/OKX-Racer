import pyautogui
import time
import keyboard
import random
from threading import Thread

RESOLUTION_X = 1920
RESOLUTION_Y = 1080
CENTER_X = RESOLUTION_X / 2 
CENTER_Y = RESOLUTION_Y / 2

running = False  

print("Press 's' to start")

def toggle_running():
    global running
    running = not running
    if running:
        print("Program started")
    else:
        print("Program stopped")

def main():
    keyboard.add_hotkey('s', toggle_running)

    while True:
        if running:
            # pyautogui.moveTo(CENTER_X, CENTER_Y, duration=1, tween=pyautogui.easeOutQuad)
            MoveToButton("Buttons.png")
            OpenLong()
            print()
        if running:
            MoveToButton("Buttons.png")
            OpenShort()
            print()
        time.sleep(0.1)  

def OpenLong():
    X_random =random.randint(-30,30)
    Y_random =random.randint(-15,15)
    print("Wait for Click")
    pyautogui.move(-100 + X_random, 0 + Y_random, duration=0.8, tween=pyautogui.easeOutQuad)
    pyautogui.click(button="left")
    print("Long was open")
    time.sleep(8)
    print("Long was closed")

def OpenShort():
    X_random =random.randint(-30,30)
    Y_random =random.randint(-15,15)
    print("Wait for Click")
    pyautogui.move(100 + X_random, 0 + Y_random, duration=0.8, tween=pyautogui.easeOutQuad)
    pyautogui.click(button="left")
    print("Short was open")
    time.sleep(8)
    print("Short was closed")

def MoveToButton(img):
    Button_Location = pyautogui.locateOnScreen(image=img, confidence=0.9)
    if Button_Location is not None:
        print(f"Image ({img}) has been found!")
        Button_Point = pyautogui.center(Button_Location)
        pyautogui.moveTo(Button_Point.x, Button_Point.y, duration=0.5, tween=pyautogui.easeOutQuad)
    else:
        print(f"Your image ({img}) hasn't been found!")

if __name__ == "__main__":
    main()
