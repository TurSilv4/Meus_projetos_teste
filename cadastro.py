from datetime import date
import getpass

base_dados = list()
login_senha = list()
user = dict()
user_login = dict()

user['Nome'] = str(input('Nome: ')).strip().title()
user['Ano_nascimento'] = int(input('Ano de nascimento: '))
user['Idade'] = date.today().year - user['Ano_nascimento']
user['Email'] = str(input('Email de cadastro: ')).strip().lower()
user['Telefone'] = int(input('Número de telefone: '))
user_login['Login'] = getpass.getuser('Login: ')
user_login['Senha'] = getpass.getpass('Password: ')
login_senha.append(user_login.copy())
user_login.clear()
base_dados.append(user.copy())
user.clear()
