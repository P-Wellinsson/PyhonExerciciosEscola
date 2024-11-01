saq = int(input('Digite quanto você quer sacar:R$'))
n100 = saq// 100
n10 = (saq% 100)// 10
n1 = saq% 10

if 10 <= saq <= 600:
    not100 = f'{n100} notas de R$100' if n100 > 1 or n100 == 0 else '1 nota de R$100'
    saq = saq - (n100 * 100)

    not50 = f'1 nota de R$50' if saq >= 50 else f'0 notas de R$50'
    saq = saq - 50 if saq >= 50 else saq - 0

    n10 = (saq - n10 * 10) - 5 if saq >= 50 else (saq - n1)// 10
    not10 = f'{n10} notas de R$10' if n10 > 1 or n10 == 0 else '1 nota de R$10'
    saq = saq - (n10 * 10)

    not5 = f'1 nota de R$5' if saq >= 5 else f'0 notas de R$5'
    saq = saq - 5 if saq >= 5 else saq - 0

    not1 = f'{saq} notas de R$1' if saq > 1 or saq == 0 else '1 nota de 1R$'

    print(f'O programa fornece: \n{not100} \n{not50} \n{not10} \n{not5} \n{not1}')
else:
    print('Valor Inválido')
