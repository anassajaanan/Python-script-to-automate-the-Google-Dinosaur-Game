import pyautogui
from PIL import Image
import time


def play(num):
    for i in range(10000):
        time.sleep(0.00000000001)
        pyautogui.screenshot(f"img/screenshot.png", region=(600, 330, num, 95))
        s = Image.open(f"img/screenshot.png")
        for x in range(s.width):
            for y in range(s.height):
                if s.getpixel((x, y)) == (83, 83, 83):
                    print(i, s.getpixel((x, y)))
                    pyautogui.press("Space")
                    play(num + 0.7)


time.sleep(3)
pyautogui.press('Space')
play(65)
