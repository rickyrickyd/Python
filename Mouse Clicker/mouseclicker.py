import pyautogui
import time
time.sleep(3)
print(pyautogui.position())
print(pyautogui.size())

for i in range(500):
    pyautogui.tripleClick(interval=0.001)
    pyautogui.click(x=1398, y=500, clicks=500, interval=0.001, button='left')

     