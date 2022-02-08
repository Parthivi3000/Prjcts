import pyautogui
import time
def spam():
    pyautogui.hotkey("h")
    pyautogui.hotkey("e")
    pyautogui.hotkey("y")
    pyautogui.hotkey("Enter")


print("3 sec wait time")
time.sleep(1)
print(". . .")
time.sleep(1)
print(" . . ")
time.sleep(1)
print("  .  ")

for i in range (0,9999999999999999999999999):
    spam()