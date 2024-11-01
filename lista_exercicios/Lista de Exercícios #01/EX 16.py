m = float(input('Qual o tamanho da área em m²? '))
li = m / 3
la = li / 18
cust = la * 80
if int(la) == la:
    print(f'A quantidade de latas de tinta é de: {la}')
else:
    la = int(la)+1
    print(f'A quantidade de latas de tinta é de: {la}')
if m < 54:
    print('Para essa quantidade de m², você precisara de pelo menos 1 tinta, que é 80.00 reais')
else:
    print(f'O preço total é de R${la * 80 :.2f}')
