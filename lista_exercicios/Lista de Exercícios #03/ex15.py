nf = int(input('Quantidade de termos da sequência Fibonacci: '))
n1 = 0
n2 = 1
c = 3
print(f'{n1} ➩ {n2}', end=' ➩ ')
while c <= nf:
    n3 = n1 + n2
    print(n3, end=' ➩ ')
    n1 = n2
    n2 = n3
    c += 1
print('Acabou')
