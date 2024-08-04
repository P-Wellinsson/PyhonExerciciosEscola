h = float(input('Quanto você ganha por hora ? R$ '))
m = float(input('Quantas horas você trabalha no mês? '))
sb = h * m
inss = sb * (8/100)
sind = sb * (5/100)
print('O salário bruto é: {}'.format(sb))
print('Você pagou {} para o INSS'.format(inss))
print('Você pagou {} para o Sindicato.'.format(sind))
print('O valor do seu sálario liquido é de {}'.format(sb - inss - sind - sb *(11/100)))
