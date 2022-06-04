import getpass
import PySimpleGUI as sg

layout = [
    [sg.Text('Login')],
    [sg.InputText(key='Login')],
    [sg.InputText(key='password')],
    [sg.Button('Login')],
    [sg.Text('', key='msg')]
]

janela = sg.Window('Login', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Login':
        janela['msg'].update('Login efetuado com sucesso!')


janela.close()