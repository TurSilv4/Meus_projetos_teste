1
#  SISTEMA

import random
from time import sleep


def linha():
    print('-' * 30)

def leiaInt(str):
    """Lẽ numeros inteiros já com validação de dados"""
    while True:
        try:
            user = int(input(str))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor informe um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            return 0
        else:
            return user

#  GAME
def game(player_1, player_2):
    if player_1 == player_2:
        print('Empate! Mais uma vez...')
        sleep (1)
        print('[ 1 ] Pedra\n'
              '[ 2 ] Papel\n'
              '[ 3 ] Tesoura')
        return True

    elif player_1 == 1:
        if player_2 == 2:
            print('Jogador 2 venceu.')
        elif player_2 == 3:
            print('Jogador 1 venceu.')

    elif player_1 == 2:
        if player_2 == 1:
            print('Jogador 1 venceu')
        elif player_2 == 3:
            print('Jogador 2 venceu')

    elif player_1 == 3:
        if player_2 == 1:
            print('Jogador 2 venceu')
        elif player_2 == 2:
            print('Jogador 1 venceu')



opçoes = ['Pedra', 'Papel', 'Tesoura']  # LISTA DE OPÇÕES JOGÁVEIS

#  PROGRAMA

print(f'{"JO-KEN-PO":^40}')
print('-'*40)
print(f'{"MENU:":<40}')
print('-'*40)
print('MODO DE JOGO:')
print('''[ 1 ] IA
[ 2 ] PVP''')

gameMode = leiaInt('► ')  # INPUT JOGADOR (modo de jogo)

while gameMode not in range (1, 3):  # LAÇO VERIFICA SE A OPÇÃO É VALIDA
    print('\033[0;31mERRO: por favor informe um valor inteiro válido.\033[m')
    gameMode = leiaInt('► ')

linha()

#  MODOS DE JOGO

# IA
print('CERTO! EU SOU O JOGADOR 1 E VOCÊ O JOGADOR 2')
if gameMode == 1:
    print('[ 1 ] Pedra\n'
          '[ 2 ] Papel\n'
          '[ 3 ] Tesoura')
    linha()
    
    empate = True
    while empate:  # LAÇO PRA SE CASO HAJA EMPATE REINICIE O CICLO

        player_1 = random.randint(1, 3)  # GERA A ESCOLHA DO COMPUTADOR
        player_2 = leiaInt(' Sua escolha: ')  # INPUT DA OPÇÃO DO JOGADOR

        while player_2 not in range(1, 4):  # LAÇO QUE VERIFICA SE A OPÇÃO É VALIDA
            print('\033[0;31mERRO: por favor informe um valor inteiro válido.\033[m')
            player_2 = leiaInt(' Sua escolha: ')
        linha()
        print(f'Eu escolhi: {opçoes[player_1-1]}')
        linha
        sleep (1)
        print(f'Você escolheu: {opçoes[player_2-1]}\n')

        print('PEDRA')
        sleep (1)
        print('PAPEL')
        sleep (1)
        print('TESOURA')
        sleep (1)
        linha()
        empate = game(player_1, player_2)  #SISTEMA DO JOGO










# PVP

else:
    pass



















