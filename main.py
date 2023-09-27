import pyautogui
import pandas
import time

pyautogui.press('win')
pyautogui.write('opera gx')
pyautogui.press('Enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

time.sleep(2)

pyautogui.write(link)
pyautogui.press('Enter')

time.sleep(3)

pyautogui.click(x=888, y=394, clicks=3)
pyautogui.press('Del')
pyautogui.write('pythonimpressionador@gmail.com')

pyautogui.press('Tab')
pyautogui.press('Del')
pyautogui.write('senha qualquer aqui')

pyautogui.press('Enter')

time.sleep(3)

tabela = pandas.read_csv('produtos.csv')

for i in tabela.index:

  codigo = tabela.loc[i, 'codigo']
  marca = tabela.loc[i, 'marca']
  tipo = tabela.loc[i, 'tipo']
  categoria = tabela.loc[i, 'categoria']
  preco = tabela.loc[i, 'preco_unitario']
  custo = tabela.loc[i, 'custo']
  obs = tabela.loc[i, 'obs']

  pyautogui.click(x=767, y=274, clicks=3)
  pyautogui.press('Del')
  pyautogui.write(str(codigo))

  pyautogui.press('Tab')
  pyautogui.write(str(marca))

  pyautogui.press('Tab')
  pyautogui.write(str(tipo))

  pyautogui.press('Tab')
  pyautogui.write(str(categoria))

  pyautogui.press('Tab')
  pyautogui.write(str(preco))

  pyautogui.press('Tab')
  pyautogui.write(str(custo))
  pyautogui.press('Tab')

  if not pandas.isna(obs):
    pyautogui.write(str(obs))

  pyautogui.press('Tab')
  pyautogui.press('Enter')

  pyautogui.scroll(50000)