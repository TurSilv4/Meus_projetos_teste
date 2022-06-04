import pyautogui as py
from time import sleep

linhas = int(input('Qual o tamanho da msg: '))
msg = str(input('Mensagem: '))
cont = 0
sleep(2)
while cont < linhas:
    py.typewrite(msg)
    py.press('Enter')
    cont += 1
