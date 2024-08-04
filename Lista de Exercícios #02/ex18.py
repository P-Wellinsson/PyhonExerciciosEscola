print('Digite abaixo uma Data no formato dd/mm/aaaa')
d = int(input('Digite o Dia: '))
m = int(input('Digite um mês: '))
a = int(input('Digite um ano: '))

if a >= 0 and 12 >= m > 0 and 0 < d <= 31:
    if m in (1, 3, 5, 7, 8, 10, 12):
        if d <= 31:
            print(f'A data {d}/{m}/{a} é uma data válida')
        else:
            print(f'A data {d}/{m}/{a} é uma data inválida')
    elif m in (4, 6, 9, 11):
        if d <= 30:
            print(f'A data {d}/{m}/{a} é uma data válida')
        else:
            print(f'A data {d}/{m}/{a} é uma data inválida')
    else:#Ano Fevereiro, 28 ou 29. Depende se é bissexto
        if d == 29 and a%4 == 0 and a != 100 or a%400 == 0:
            print(f'A data {d}/{m}/{a} é uma data válida')
        elif  d <= 28:
            print(f'A data {d}/{m}/{a} é uma data válida')
        else:
            print(f'A data {d}/{m}/{a} é uma data inválida')
else:
    print(f'A data {d}/{m}/{a} é uma data inválida')
