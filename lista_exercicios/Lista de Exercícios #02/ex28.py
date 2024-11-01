tipoCa = int(input('Digite qual tipo de carne você quer. Você pode escolher apenas 1 tipo \n(0) Filé Duplo \n(1) Alcatra \n(2) Picanha \n:'))
quant = int(input('Quantos Kg de carne você quer? '))
card = input('Você vai usar o cartão Tabajara? Com ele terá 5% de desconto. \n(S) para sim e (N) para não \n').upper()

file = quant * 4.9 if 5 >= quant >= 1 else quant * 5.8
alca = quant * 5.90 if 5 >= quant >= 1 else quant * 6.8
pican = quant * 6.9 if 5 >= quant >= 1 else quant * 7.8

if card == 'S' or card == 'N' and quant > 0:
    if tipoCa == 0: #Filé Duplo
        card = f'Com o desconto do cartão Tabajara de R${file * (5/100):.2f} \nO valor a pagar é: R${file - file * (5/100):.2f}' if card == 'S' else f'R${file:.2f} sem desconto do cartão Tabajara \nO valor a pagar é: R${file:.2f}'
        print('=-' * 22)
        print(f'Tipo de carne: Filé Duplo \nQuantidade de carne: {quant}Kg \nPreço total: R${file:.2f} \n{card}')
        print('=-' * 22)
    elif tipoCa == 1: #Alcatra
        card = f'Com o desconto do cartão Tabajara de R${alca * (5/100):.2f} \nO valor a pagar é: R${alca - alca * (5/100):.2f}' if card == 'S' else f'R${alca:.2f} sem desconto do cartão Tabajara \nO valor a pagar é: R${alca:.2f}'
        print('=-' * 22)
        print(f'Tipo de carne: Alcatra \nQuantidade de carne: {quant}Kg \nPreço total: R${alca:.2f} \n{card}')
        print('=-' * 22)
    elif tipoCa == 2: #Picanha
        card = f'Com o desconto do cartão Tabajara de R${pican * (5/100):.2f} \nO valor a pagar é: R${pican - pican * (5/100):.2f}' if card == 'S' else f'R${pican:.2f} sem desconto do cartão Tabajara \nO valor a pagar é: R${pican:.2f}'
        print('=-' * 22)
        print(f'Tipo de carne: Picanha \nQuantidade de carne: {quant}Kg \nPreço total: R${pican:.2f} \n{card}')
        print('=-' * 22)
    else:
        print('O valor do tipo da carne está incorreto')
else:
    print('Os Kg de carne, se vai usar o cartão Tabajara ou ambos estão incorretos!')
