import pyautogui
from pynput.mouse import Button, Controller
import time

a = 500

RESOLUTION_X = 1920
RESOLUTION_Y = 1080
CENTER_X = RESOLUTION_X / 2 - (a/2)
CENTER_Y = RESOLUTION_Y / 2 - (a/2)

mouse = Controller()


def main(Square_side):
    current_x = CENTER_X
    current_y = CENTER_Y
    print("Let's start!")
    mouse.position = (current_x, current_y)
   
    mouse.press(Button.left)
    while Square_side > 0:
        # Движение вправо
        for _ in range(Square_side):
            current_x += 1
            mouse.position = (current_x, current_y)
            time.sleep(0.001)  # Пауза для замедления движения (можно убрать)
        Square_side -= 15 

        # Движение вниз
        for _ in range(Square_side):
            current_y += 1
            mouse.position = (current_x, current_y)
            time.sleep(0.001)
        Square_side -= 15

        # Движение влево
        for _ in range(Square_side):
            current_x -= 1
            mouse.position = (current_x, current_y)
            time.sleep(0.001)
        Square_side -= 15

        # Движение вверх
        for _ in range(Square_side):
            current_y -= 1
            mouse.position = (current_x, current_y)
            time.sleep(0.001)

        Square_side -= 15  # Уменьшаем сторону квадрата

    mouse.release(Button.left)
    print("Well done!")

main(a)
