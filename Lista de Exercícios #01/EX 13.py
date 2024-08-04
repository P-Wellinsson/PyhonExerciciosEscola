a = float(input('Qual é a sua altura? '))
gen = input('Qual é o seu gênero? ').upper()
if gen == 'M':
    print('O seu peso ideal é: {}'.format(72.7*a - 58))
else:
    print('O seu peso ideal é: {}'.format(62.1*a - 44.7))
