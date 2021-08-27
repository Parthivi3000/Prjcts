import pyautogui    #import auto gui function in python that automates mouse and keyboard
while True:         #while loop
	try:
		pyautogui.moveTo(0, 620, duration = 3.2)       #movement of the mouse
		pyautogui.moveTo(620, 0, duration = 3.2)
		pyautogui.moveTo(300, 0, duration = 3.2)
		pyautogui.moveTo(0,300, duration = 3.2)
	except KeyboardInterrupt:                                  #added interupt ctrl+c
		quit()                              #exits the program explicitly



