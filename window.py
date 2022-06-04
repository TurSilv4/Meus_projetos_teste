import requests
from tkinter import *

def pegar_cotaçoes():
    requisiçao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisiçao_dic = requisiçao.json()

    dolar = requisiçao_dic['USDBRL']['bid']
    euro = requisiçao_dic['EURBRL']['bid']
    BTC = requisiçao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar {dolar}
    Euro {euro}
    BTC {BTC}'''

pegar_cotaçoes()

# Janela

janela = Tk() #Abre a janela
janela.title('Login')
#janela.geometry('250x150')
texto_login = Label(janela, text='  Login de usuário:')
texto_login.grid(column=0, row=2)
user_name = Entry(janela, show=None, font=('Arial', 12))
user_password = Entry(janela, show= '*', font=('Arial', 12 ))
user_name.pack()
user_password.pack()


janela.mainloop() #Mantem a janela aberta