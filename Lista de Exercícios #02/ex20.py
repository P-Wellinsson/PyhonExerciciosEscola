n = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
n3 = float(input('Digite a 3º nota: '))
med = (n + n2 +n3)/ 3
if med == 10:
    print(f'Aprovado com Distinção \nVocê tirou {med:.1f} no total')
elif 7 <= med < 10:
    print(f'Aprovado \nVocê tirou {med:.1f} no total')
elif 0 <= med < 7:
    print(f'Reprovado \nVocê tirou {med:.1f} no total')
else:
    print('Valor Inválido!!')
