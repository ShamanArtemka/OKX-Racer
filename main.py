import pyautogui
import time
import keyboard
from threading import Thread

RESOLUTION_X = 1920
RESOLUTION_Y = 1080
CENTER_X = RESOLUTION_X / 2 
CENTER_Y = RESOLUTION_Y / 2

running = False  # Переменная состояния

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
            MoveToButton("Buttons.png")
            OpenShort()
        time.sleep(0.1)  

def OpenLong():
    print("Wait for Click")
    pyautogui.move(-30, 0, duration=0.8, tween=pyautogui.easeOutQuad)
    pyautogui.click(button="left")
    print("Long was open")
    time.sleep(10)
    print("Long was closed")

def OpenShort():
    print("Wait for Click")
    pyautogui.move(30, 0, duration=0.8, tween=pyautogui.easeOutQuad)
    pyautogui.click(button="left")
    print("Short was open")
    time.sleep(10)
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
