def linha(txt):
    print(f'\033[7;40m{txt.center(30)}\033[m')


def user_input(txt):
    while True:
        try:
            user = str(input(txt)).strip().title()
            while user not in ('Pedra', 'Papel', 'Tesoura'):
                print('Escolha uma opção válida!')
                user = str(input(txt)).strip().title()
        except:
            print('Escolha um valor válido!')
        else:
            return user

def escolhas(player_1, player_2):
    opcoes = 'Pedra', 'Papel', 'Tesoura'
    for cont, opcao in enumerate(lista):
        if player_1 == 'Pedra':
            if player_2 == opcao[cont]:
                pass