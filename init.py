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

for linha in tabela.index:

    pyautogui.click(x=1213, y=249   )

    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)