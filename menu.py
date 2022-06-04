
def menu(str):
    print('-=' * 20)
    print(f'{str:^40}')
    print('=-' * 20)


def subtitle(str):
    print('=-' * 15)
    print(f'► {str:^26} ◄')
    print('-' * 30)


def linha():
    print('-' * 30)
#Programa principal
while True:
    menu('MENU')
    print('Opções:')
    linha()
    print('''[ 1 ] Fazer login
[ 2 ] Novo cadastro''')
    user = int(input('► ')) # Usuario
    while user > 2:
        print('Escolha uma opção válida: [1 / 2]')
        user = int(input('► '))

    if user == 1:
        subtitle('Login')
        import login # Abre o aquivo de login

    elif user == 2:
        subtitle('Novo cadastro')
        import cadastro # Abre o arquivo de cadastro
        linha()
        print('Cadastro realizado com sucesso.')
    subtitle('O que deseja: ')
    print('''[ 1 ] Voltar ao MENU.
[ 2 ] ENcerrar o programa..''')

    user = int(input('► '))
    while user > 2:
        user = int(input('ERRO! Escolha uma opção válida: '))
    if user == 2: # Encerra programa
        linha()
        print('ENCERRANDO...')
        break
