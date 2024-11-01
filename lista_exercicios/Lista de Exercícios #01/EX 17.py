from math import ceil

m = float(input('Digite o tamanho em m²: '))
litro = ceil(m/ 6 * (10/100) + m/ 6)
lata = ceil(litro // 18)
galão = ceil((litro % 18)/ 3.6)
preço = lata * 80 + galão * 25

print('\nUma lata de tinta com 18 litros custa R$80,00. \nE um galão de tinta com 3,6 litros custa R$25,00.')
print(f'\nVocê precisa de {litro} litro(s) de tinta \nVocê vai precisar de {lata} lata(s) e {galão} galão(ões).')
print(f'O total em dinheiro de tudo é de R${preço:.2f}')
