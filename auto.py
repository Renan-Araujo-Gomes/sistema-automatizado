import pyautogui
import time

pyautogui.alert("O código vai começar.")
pyautogui.PAUSE = 0.5

pyautogui.press('winleft')
pyautogui.write('Google')
pyautogui.press('enter')

pyautogui.write('https://drive.google.com')
pyautogui.press('enter')

pyautogui.hotkey('winleft','d')

pyautogui.moveTo(567,38)
pyautogui.mouseDown()
pyautogui.moveTo(756,635)


pyautogui.hotkey('alt','tab')

pyautogui.mouseUp()

time.sleep(5)