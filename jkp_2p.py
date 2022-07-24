from back_jokenpo_2p import *


while True:
    game_mode = menu('JO-KEN-PO', 'MENU')
    while game_mode not in range(1, 3):
        print('Escolha um opção válida!')
        game_mode = leiaInt('► ')
    if game_mode == 1:
        player_1, player_2 = players()
        print(player_1, player_2)