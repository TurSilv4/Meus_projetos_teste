cardapio = [('Calabresa', 20), ('Mussarela', 23), ('Presunto', 20), ('Milho', 27), ('Atum', 30)]

print('Escolha o sabor de sua pizza:')
print('='*30)
print(f'{"Num.":4} {"Sabores":20} Valores')
for numeroItem, sabor in enumerate(cardapio):
    print(f'{numeroItem+1:<3}- {sabor[0]:20} R${sabor[1]:.2f}')
