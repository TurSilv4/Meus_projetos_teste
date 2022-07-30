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
    global score_player_1, score_player_2, score
    try:
        if player_1 == player_2:
            return 'Empate! Mais uma vez...'

        elif player_1 == 'Pedra':
            if player_2 == 'Papel':
                score_player_2 += 1
                return 'Jogador 2 venceu.'
            elif player_2 == 'Tesoura':
                score_player_1 += 1
                return 'Jogador 1 venceu.'

        elif player_1 == 'Papel':
            if player_2 == 'Pedra':
                score_player_1 += 1
                return 'Jogador 1 venceu'
            elif player_2 == 'Tesoura':
                score_player_2 += 1
                return 'Jogador 2 venceu'

        elif player_1 == 'Tesoura':
            if player_2 == 'Pedra':
                score_player_2 += 1
                return 'Jogador 2 venceu'
            elif player_2 == 'Papel':
                score_player_1 += 1
                return 'Jogador 1 venceu'
    finally:
        score = (score_player_1, score_player_2)
        return score


def vencedor(player_1_score, player_2_score):
    if player_1_score > 2:
        return 'Jogador 1 venceu!'
    elif player_2_score > 2:
        return 'Jogador 2 venceu!'

