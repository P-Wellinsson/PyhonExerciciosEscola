p = float(input('Qual é o peso dos peixes? '))

if p <= 50:
    print('Você não passou do limete de peso ')
else:
    e = (p - 50)
    print('O dinheiro que você tem que pagar por causa da multa é de R${:.2f}'.format(e * 4))
