def cabecalho(txt):
    print(f'\033[7;40m{txt.center(30)}\033[m')


def linha():
    print('-' * 30)


def player_choice(txt):
    while True:
        try:
            player = str(input(txt)).strip().title()
            while player not in ('Pedra', 'Papel', 'Tesoura'):
                print(
'''Escolha uma opção válida!
 - Pedra
 - Papel
 - Tesoura''')
                player = str(input(txt)).strip().title()
        except:
            print('Escolha um valor válido!')
        else:
            return player


def players(player_1, player_2):
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