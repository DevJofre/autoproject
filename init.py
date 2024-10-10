import pyautogui;
import time;

#--------------------------------

pyautogui.PAUSE = 0.5

#--------------------------------

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=689, y=477)

#--------------------------------

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

#--------------------------------

pyautogui.click(x=1215, y=352)
pyautogui.write("rakaialbion@gmail.com")
pyautogui.press("tab")
pyautogui.write("rakai123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

#--------------------------------

