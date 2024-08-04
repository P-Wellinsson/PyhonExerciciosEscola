me = ma = s = c = 0
while True:
    n = int(input('Digite um número: '))
    c += 1
    if c == 1 or n < me:
        me = n
    ma = ma if ma > n else n
    s += n
    while True:
        stop = input('Quer parar? [S/N]').strip().upper()[0]
        if stop in ('SN'):
            break
    if stop == 'S':
        break
print(f'Dos {c} valores, o menor valor é {me}, o maior é {ma} e a soma dos valores é {s}')
