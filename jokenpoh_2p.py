print('Vamos brincar de JOKENPÔ?')
print('Escolha entre \n Pedra\n Papel\n Tesoura')
player_1 = str(input('Jogador 1')).strip().title()
player_2 = str(input('Jogador 2')).strip().title()
print('Você escolheu {}\n'
      'Eu escolhi {}'.format(player_1, computador))
if player_1 == computador:
    print('Olha! Deu empate\n Vamos jogar denovo?')
elif player_1 == 'Pedra':
    if computador == 'Papel':
        print('HAHAHA... Eu ganhei')
    elif computador == 'Tesoura':
        print('AAAH! Você ganhou.')
elif player_1 == 'Papel':
    if computador == 'Pedra':
        print('AAAH! Você ganhou.')
    elif computador == 'Tesoura':
        print('HAHAHA... Eu ganhei.')
elif player_1 == 'Tesoura':
    if computador == 'Pedra':
        print('HAHAHA... Eu ganhei.')
    elif computador == 'Papel':
        print('AAAH! Você ganhou.')
else:
    print('JOGADA INVÁLIDA\n TENTE NOVAMENTE!')
