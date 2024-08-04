from math import sqrt
a = float(input('Digite o valor de "a": '))
b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))
d = (b**2)-4 * a * c

if a == 0:
    print('Essa não é uma equação do segundo grau! ')
else:
    if d < 0:
        print('A equação não possui raízes reais! ')
    else:
        if d == 0:
            print('A equação possui apenas 1 raiz! ')
        if d > 0:
            x1 = (-b + d ** 0.5)/ 2*a
            x2 = (-b - d ** 0.5)/ 2*a
            print(f'A equação possui duas raízes reais que são: {x1} e {x2}')
