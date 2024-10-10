import pyautogui;
import time;
import pandas;

#----------------------------------

pyautogui.PAUSE = 0.5

#----------------------------------

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=689, y=477)

#----------------------------------

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

#----------------------------------

pyautogui.press("tab")
pyautogui.write("rakaialbion@gmail.com")
pyautogui.press("tab")
pyautogui.write("rakai123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

#----------------------------------

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#----------------------------------

pyautogui.press("tab")
pyautogui.write("codigo")

pyautogui.press("tab")
pyautogui.write("Marca do Produto")

pyautogui.press("tab")
pyautogui.write("Tipo do Produto")

pyautogui.press("tab")
pyautogui.write("Categoria do Produto")

pyautogui.press("tab")
pyautogui.write("Preço Unitário do Produto")

pyautogui.press("tab")
pyautogui.write("Custo do Produto")

pyautogui.press("tab")
pyautogui.write("OBS")

pyautogui.press("tab")
pyautogui.press("enter")