from random import choice
print('Vamos brincar de JOKENPÔ?')
print('Escolha entre \n Pedra\n Papel\n Tesoura')
jogador = str(input('')).strip().title()
lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)
print('Você escolheu {}\n'
      'Eu escolhi {}'.format(jogador, computador))
if jogador == computador:
    print('Olha! Deu empate\n Vamos jogar denovo?')
elif jogador == 'Pedra':
    if computador == 'Papel':
        print('HAHAHA... Eu ganhei')
    elif computador == 'Tesoura':
        print('AAAH! Você ganhou.')
elif jogador == 'Papel':
    if computador == 'Pedra':
        print('AAAH! Você ganhou.')
    elif computador == 'Tesoura':
        print('HAHAHA... Eu ganhei.')
elif jogador == 'Tesoura':
    if computador == 'Pedra':
        print('HAHAHA... Eu ganhei.')
    elif computador == 'Papel':
        print('AAAH! Você ganhou.')
else:
    print('JOGADA INVÁLIDA\n TENTE NOVAMENTE!')
