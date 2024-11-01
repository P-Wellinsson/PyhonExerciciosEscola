while True:
    prim = 0
    n = int(input('Digite um número para saber se é ou não um número primo: '))
    for i in range(1 ,n + 1):
        if n % i == 0:
            prim += 1
    if prim == 2:
        print('Esse é um número primo! ')
    else:
        print('Não é um número primo')
