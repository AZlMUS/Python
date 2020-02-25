import pyautogui
import time
x=0

pyautogui.hotkey("alt","tab")
pyautogui.hotkey("ctrl","c")
pyautogui.keyDown("alt")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.keyUp("alt")
time.sleep(2)
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("alt","tab")
pyautogui.press("down")

while x!=23:
	pyautogui.hotkey("ctrl","c")
	pyautogui.hotkey("alt","tab")
	pyautogui.hotkey("ctrl","v")
	pyautogui.press("enter")
	pyautogui.keyDown("alt")
	time.sleep(2)
	pyautogui.press("tab")	
	time.sleep(2)
	pyautogui.keyUp("alt")
	pyautogui.press("down")
	x=x+1
	time.sleep(1)

