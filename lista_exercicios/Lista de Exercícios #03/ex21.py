cont = 's'
while not cont == 'N':
    cont = 's'
    prim = 0
    n = int(input('Digite um número inteiro: '))
    for i in range(1, n + 1):
        if n % i == 0:
            prim += 1
    if prim == 2:
        print('Esse é um número primo! ')
    else:
        print('Não é um número primo! ')
    while cont not in ('SN'):
        cont = input('Continuar [S/N]').strip().upper()[0]
print('\nObrigado pela preferência.')
