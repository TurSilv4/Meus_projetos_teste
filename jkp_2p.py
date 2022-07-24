from back_jokenpo_2p import *


while True:
    game_mode = menu('JO-KEN-PO', 'MENU')
    if game_mode not in range(1, 3):
        print('Escolha um opção válida!')
        game_mode = leiaInt('► ')
