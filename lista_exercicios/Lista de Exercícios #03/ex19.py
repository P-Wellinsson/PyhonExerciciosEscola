me = ma = som = c = 0
while True:
    n = int(input('\nDigite um número entre 0 e 1000: '))
    while not 0 < n <= 1000:
        n = int(input('\nNúmero incorreto, digite novamente \nDigite um número entre 0 e 1000: '))
    c += 1
    me = n if c == 1 or n < me else me
    ma = n if n > ma else ma
    som += n
    while True:
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
        if resp in ('SN'):
            break
    if resp == 'N':
        break
print(f'Foram {c} números, o menor deles foi o {me}, o maior {ma} e a soma deles foi {som}')
