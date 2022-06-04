from random import choice
from time import sleep
print('\033[34m=-' * 14)
print('\033[36m         JO-KEN-PÔ')
print('\033[34m=-\033[m' * 14)
print('Vamos brincar de JO-KEN-Pô?\n'
      ' Escolha entre:\n'
      '  Pedra\n'
      '  Papel\n'
      '  Tesoura')
print()
jogador = str(input('')).strip().title()
lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)
sleep(0.5)
print('\033[36m')
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
print('\033[m')
if jogador == computador:
    print('Olha! Deu empate\n Vamos jogar denovo?')
elif jogador == 'Pedra':
    if computador == 'Papel':
        print(' HAHAHA... Eu ganhei!')
    elif computador == 'Tesoura':
        print(' AAAH! Você ganhou!')
elif jogador == 'Papel':
    if computador == 'Pedra':
        print(' AAAH! Você ganhou!')
    elif computador == 'Tesoura':
        print(' HAHAHA... Eu ganhei')
elif jogador == 'Tesoura':
    if computador == 'Pedra':
        print(' HAHAHA... Eu ganhei!')
    elif computador == 'Papel':
        print(' AAAH! Você ganhou!')
else:
    print('JOGADA INVÁLIDA\n JOGUE NOVAMENTE')
print('')
print('Você escolheu: {}'.format(jogador))
print('E eu: {}'.format(computador))
