from random import choice
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
print('-=-' * 10)
print('Vamos brincar de JO-KEN-PÔ?')
print('-=-' * 10)
sleep(1)
eu = str(input('Escolha entre Pedra, Papel e Tesoura: \n Relaxa que eu não vou olhar não HEHEHE...')).strip()
print(' ')
if eu == 'pedra':
    print('Eu escolhi {} \n E você {}'.format(pc, eu))
    print(' ')
    sleep(1)
    if pc == 'pedra':
        print('OLha! Deu empate.\n Vamos denovo?')
    elif pc == 'tesoura':
        print('AAAH! Você ganhou! \n PARABENS.')
    elif pc == 'papel':
        print('HAHAHA... Eu ganhei!')
    else:
        print('JOGADA INVÁLIDA\n TENTE NOVAMENTE')
if eu == 'tesoura':
    print('Eu escolhi {} \n E você {}'.format(pc, eu))
    print(' ')
    sleep(1)
    if pc == 'pedra':
        print('HAHAHA... Eu ganhei!')
    elif pc == 'papel':
        print('AAAH! Você ganhou! \n PARABENS.')
    elif pc == 'tesoura':
        print('OLha! Deu empate \n Vamos denovo?')
    else:
        print('JOGADA INVÁLIDA\n TENTE NOVAMENTE')
if eu == 'papel':
    print('Eu escolhi {} \n E você {}'.format(pc, eu))
    print(' ')
    sleep(1)
    if pc == 'pedra':
        print('AAAH! Voce ganhou! \n PARABENS.')
    elif pc == 'papel':
        print('Olha! Deu empate \n Vamos denovo?')
    elif pc == 'tesoura':
        print('HAHAHA... Eu ganhei!')
    else:
        print('JOGADA INVÁLIDA\n TENTE NOVAMENTE')
