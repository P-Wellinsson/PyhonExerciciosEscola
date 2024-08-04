n = int(input('Digite um número para ser o fatorial: '))
fac = 1
print(f'{n}! = ', end='')

for i in range(1, n + 1):
    print(f'{n}', end='')
    print(f' X ' if n > 1 else ' = ', end='')
    fac *= n
    n -= 1
print(fac, end='')
