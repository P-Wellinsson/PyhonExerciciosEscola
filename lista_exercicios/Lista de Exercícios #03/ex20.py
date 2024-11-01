#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
cont = 's'
while cont != 'N':
    cont = 's'
    n = int(input('Digite um número inteiro, positivo e menor que 16 para o fatorial: '))
    fat = 1
    while True:
        if n >= 16:
            n = int(input('O número tem que ser menor que 16. \nDigite um número inteiro, positivo e menor que 16 para o fatorial: '))
        elif n < 0:
                n = int(input('Tem que ser um número positivo. \nDigite um número inteiro, positivo e menor que 16 para o fatorial: '))
        else:
            print(f'{n}!', end=' = ')
            break
    for i in range(1, n + 1):
        fat *= i
        print(f'{n}', end='')
        print(' X ' if  n > 1 else ' = ', end='')
        n -= 1
    print(fat)
    while cont not in('SN'):
        cont = input('\nQuer continuar? [S/N]').strip().upper()[0]
fim = 'Obrigado pela preferência'
print(f'\n{fim:^140}')
