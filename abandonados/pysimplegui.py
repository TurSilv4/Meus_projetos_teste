import PySimpleGUI as sg
from pegarcotacoes import pegar_cotaçoes

#Layout
layout = [
    [sg.Text('Pegar cotação da moeda.')],
    [sg.InputText(key='nome_cotação')],
    [sg.Button('Pegar cotação'), sg.Button('Cancelar')],
    [sg.Text('', key='Texto_cotação')]
] #ELEMENTOS

# Janela
janela = sg.Window('Sistema de cotações', layout)

#Eventos
while True: # MANTEM O PROGRAMA ABERTO
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Pegar cotação':
        codigo_cotação = valores['nome_cotação']
        cotacao = pegar_cotaçoes(codigo_cotação)
        janela['Texto_cotação'].update(f'A cotação do {codigo_cotação} é de R${cotacao}')

janela.close() # FECHA A JANELA
