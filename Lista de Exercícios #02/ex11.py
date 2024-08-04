sal = float(input('Qual é o seu salário R$'))
if sal < 280 and sal > 0:
    sal1 = sal + sal*(20/100)
    print(f'Antes do reajuste o seu salário era de: R${sal}')
    print('O seu salário foi aumentado em 20% ')
    print(f'O valor de aumento do seu salário foi de: R${sal * (20/100)}')
    print(f'O seu novo salário é de R${sal1}')
elif sal >= 280 and sal < 700:
    sal2 = sal + sal*(15/100)
    print(f'Antes do reajuste o seu salário era de: R${sal}')
    print('O seu salário foi aumentado em 15% ')
    print(f'O valor de aumento do seu salário foi de: R${sal * (15/100)}')
    print(f'O seu novo salário é de R${sal2}')
elif sal >= 700 and sal < 1500:
    sal3 = sal + sal*(10/100)
    print(f'Antes do reajuste o seu salário era de: R${sal}')
    print('O seu salário foi aumentado em 10% ')
    print(f'O valor de aumento do seu salário foi de: R${sal * (10/100)}')
    print(f'O seu novo salário é de R${sal3}')
elif sal >= 1500:
    sal4 = sal + sal*(5/100)
    print(f'Antes do reajuste o seu salário era de: R${sal}')
    print('O seu salário foi aumentado em 5% ')
    print(f'O valor de aumento do seu salário foi de: R${sal * (5/100)}')
    print(f'O seu novo salário é de R${sal4}')
else:
    print('Valor indisponível')
