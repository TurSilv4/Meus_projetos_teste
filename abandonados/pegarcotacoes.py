import requests


def pegar_cotaçoes(codigo_moeda):
    try:

        requisiçao = requests.get(f'https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL')

        requisiçao_dic = requisiçao.json()

        cotacao = requisiçao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        print('Codigo de moeda inválido!')
        return None
