moKg = int(input('Quantos Kg de morango você vai querer? '))
maKg = int(input('Quantos Kg de maçã você vai querer? '))

moVal = moKg * 2.5 if 5 >= moKg >= 1 else moKg * 2.2
maVal = maKg * 1.8 if 5 >= maKg >= 1 else maKg * 1.5
Vtot = moVal + maVal

if moKg + maKg > 8 or Vtot > 25:
    print(f'O valor a ser pago é de R${Vtot - Vtot * (10/100):.2f} desconto')
elif moKg == 0 and maKg == 0:
    print('A quantidade de Kg não pode ser 0')
else:
    print(f'O valor a ser pago é de R${Vtot:.2f}')
