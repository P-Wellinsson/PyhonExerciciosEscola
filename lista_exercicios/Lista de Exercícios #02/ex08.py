p1 = float(input('Digite o valor do produto: '))
p2 = float(input('Digite o valor do produto: '))
p3 = float(input('Digite o valor do produto: '))
if p1 <  p2 and p1 < p3:
    print(f'O produto com o menor preço é o que custa {p1}')
elif p2 < p3 and p2 < p1:
    print(f'O produto com o menor preço é o que custa {p2}')
elif p3 < p1 and p3 < p2:
    print(f'O produto com o menor preço é o que custa {p3}')
elif p1 == p2 and p1 == p3:
    print(f'Os produtos custam o mesmo preço ')
else:
    print('Dois produtos custam o mesmo preço')
