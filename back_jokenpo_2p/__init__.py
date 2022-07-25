def cabecalho(txt):
    print(f'\033[7;40m{txt.center(30)}\033[m')


def linha():
    print('-' * 30)


def player_choice(txt):
    linha()
    print('► Pedra   ► Papel   ► Tesoura')
    linha()
    while True:
        try:
            player = str(input(txt)).strip().title()
            while player not in ('Pedra', 'Papel', 'Tesoura'):
                print('Escolha uma opção válida!')
                player = str(input(txt)).strip().title()
        except:
            print('Escolha um valor válido!')
        else:
            return player


def players():
    player_1 = player_choice('Sua escolha: ')
    player_2 = player_choice('Sua escolha: ')
    return player_1, player_2


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


def menu(cabecalho_1, cabecalho_2):
    cabecalho(cabecalho_1)
    linha()
    cabecalho(cabecalho_2)
    print(
'''Modo de jogo:
 [ 1 ] PvP
 [ 2 ] Melhor de 3''')
    user = leiaInt('► ')
    return user


def game(player_1, player_2, pontuacao=False):
    p1, p2 = 0

    if player_1 == player_2:
        return 'Empate! Mais uma vez...'

    elif player_1 == 'Pedra':
        if player_2 == 'Papel':
            p2 += 1
            return 'Jogador 2 venceu.', p2
        elif player_2 == 'Tesoura':
            p1 += 1
            return 'Jogador 1 venceu.', p1

    elif player_1 == 'Papel':
        if player_2 == 'Pedra':
            return 'Jogador 1 venceu'
        elif player_2 == 'Tesoura':
            return 'Jogador 2 venceu'

    elif player_1 == 'Tesoura':
        if player_2 == 'Pedra':
            return 'Jogador 2 venceu'
        elif player_2 == 'Papel':
            return 'Jogador 1 venceu'