import getpass
from datetime import date
def opçao(msg):
    print('=' * 30)
    print(f'{msg:^30}')
    print('=' * 30)
def linha():
    print('-' * 30)
data = list()
users = dict()
#Programa principal
    # Menu / opções
while True:
    opçao('MENU')

    print('[ 1 ] Novo Cadastro\n[ 2 ] Fazer login')
    linha()
    menu = int(input('► '))
    while menu > 2:
        menu = int(input('ERRO! INFORME UMA OPÇÃO VÁLIDA [1/2]\n ► '))
    linha()

    # CADASTRO
    if menu == 1:
        user = str(input('Username: ')).strip()
        users['Username'] = user[:]
        users['Nome'] = str(input('Nome completo: ')).strip().title()
        users['Nascimento'] = int(input('Ano de nascimento: '))
        users['Idade'] = date.today().year - users['Nascimento']
        user = str(input('Sexo: [M/F] ')).strip().upper()[0]
        while user not in 'MF':
            user = str(input('Informe uma opção válida: [M/F] ')).strip().upper()[0]
        users['Sexo'] = user[:]
        users['Email'] = str(input('Email: '))

        user_password = str(input('Password: ')).strip()
        user_password_confirm = str(input('Confirme a senha: ')).strip()
        if user_password == user_password_confirm:
            users['Senha'] = user_password
        else:
            user_password_confirm = str(input('As senhas são diferentes:\n Confirme a senha: '))
            users['Senha'] = user_password
        data.append(users.copy())
        users.clear()
        linha()
        print('CADASTRO CONCLUIDO!')
        linha()
        sair = str(input('Deseja voltar ao MENU? [S/N] ')).strip().upper()[0]
        while sair not in 'SN':
            sair = str(input('Opção inválida: [S/N] ')).strip().upper()[0]
        if sair == 'N':
            break
    # LOGIN
    elif menu == 2:
        username = str(input('Username: ')).strip() #Nome de usuario
        for d in data: #Pra cada dicionario na lista
            if username == d['Username']: #Verifica o nome de usuario no dicionario
                password = str(input('Password: ')).strip()
                if password == d['Senha']:
                    linha()
                    print('Login efetuado com sucesso!')
                    linha()
                    opçao('SEU MENU')
                else:
                    while password != d['Senha']:
                        print('Senha inválida!')
                        password = str(input('Password'))
            else:
                while username not in d['Username']:
                    print('Username inválido!')
                    username = str(input('Username: '))

    else:
        while menu > 2:
            menu = int(input('ERRO! INFORME UMA OPÇÃO VÁLIDA [1/2]\n ► '))
        linha()
print(data)
