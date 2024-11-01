tipo = int(input('Qual tipo de conbustível você quer? \n(0) álcool ou (1)gasolina? '))
Lit = int(input('Quantos litros de conbustível você quer comprar? '))

if Lit >= 1:
    if tipo == 0:
        pa = (Lit * 1.9) - (Lit * 1.9) * (3/100) if Lit <= 20 else (Lit * 1.9) - (Lit * 1.9) * (5/100)
        print(f'O valor do combustível de álcool é de R${pa:.2f}')
    elif tipo == 1:
        pg = (Lit * 2.5) - (Lit * 2.5) * (4/100) if Lit <= 20 else (Lit * 2.5) - (Lit * 2.5) * (6/100)
        print(f'O valor do combustível de gasolina é de R${pg:.2f}')
    else:
        print('Valor Inválido! \nTipo de conbustível incorreta')
else:
    print('Valor Inválido! \nQuantidade de litros incorreta')
