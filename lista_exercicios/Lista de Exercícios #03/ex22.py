div = []
prim = 0
n = int(input('Digite um número: '))
for i in range(1, n + 1):
    if n % i == 0:
        prim += 1
        div.append(i)
if prim == 2:
    print('Esse é um número primo! ')
else:
    print(f'Não é um número primo! \nEle é divisível por {div}')
