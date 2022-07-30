from back_jokenpo_2p import *


while True:
    game_mode = menu('JO-KEN-PO', 'MENU')
    while game_mode not in range(1, 3):
        print('Escolha um opção válida!')
        game_mode = leiaInt('► ')

    if game_mode == 1:  # Modo x1
        player_1, player_2 = players()
        resultado, score = game(player_1, player_2, pontuacao=False)
        linha()
        print(f'Jogador 1 escolheu {player_1} \nJogador 2 escolheu {player_2}')
        linha()
        print(f'O resultado é: \n{resultado}')

    elif game_mode == 2:  # Melhor de três
        while True:
            player_1, player_2 = players()
            print(vencedor())

    continuar = str(input('Deseja voltar ao MENU? [S/N] ')).strip().upper()
    while continuar not in 'SsNn':
        continuar = str(input('Escolha uma opção válida [S/N] '))
    if continuar == 'N':
        break
