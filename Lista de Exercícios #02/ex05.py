n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 7 and m < 10:
    print('Aprovado. ')
elif m < 7 and m >= 0:
    print('Reprovado.')
elif m == 10:
    print('Aprovado com distinção')
else:
    print('Número inexistente')
