cardapio = [('Calabresa', 20), ('Mussarela', 23), ('Presunto', 20), ('Milho', 27), ('Atum', 30)]

print('Escolha o sabor de sua pizza:')
print('='*40)
print(f'{"Num.":4} {"Sabores":20} Valores')
for numeroItem, sabor in enumerate(cardapio):
    print(f'{numeroItem+1:<3}- {sabor[0]:20} R${sabor[1]:.2f}')

print('Seu pedido:')
user = 0
while user not in range(1, numeroItem+1):
    print('Escolha uma opção valida por favor!')
    user = int(input('Seu pedido: '))
print(f'Você escolheu a opção {user}: {cardapio[user][0]} no valor de R${cardapio[user][1]:.2f}')
userConfirmation = str(input('Correto? [S/N] ')).strip().upper()
