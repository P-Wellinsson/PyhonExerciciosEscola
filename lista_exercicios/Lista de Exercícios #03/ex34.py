divida = float(input('Digite o valor da dívida: '))
while True:
    parcel = int(input('\nVocê quer dividir em quantas parcelas? \n 1, 3, 6, 9 ou 12: '))
    if parcel == 1:
        juros = 0
    elif parcel == 3:
        juros = 10
    elif parcel == 6:
        juros = 15
    elif parcel == 9:
        juros = 20
    elif parcel == 12:
        juros = 25
    if parcel in(1, 3, 6, 9, 12):
        break
print(f'''\nValor da Dívida: R${divida:.2f}
Valor dos Juros: {juros}%
Quantidade de parcelas: {parcel}
Valor da Parcela: R${divida /parcel:.2f}''')
