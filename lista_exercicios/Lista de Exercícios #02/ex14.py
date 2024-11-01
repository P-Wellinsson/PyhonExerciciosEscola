n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2)/2
if m >= 0 and m <= 4:
    print(f'A suas duas notas são {n1} e {n2} \nA média das notas é {m}')
    print('Você tirou a nota E')
    print('Reprovado')
elif m > 4 and m <= 6:
    print(f'A suas duas notas são {n1} e {n2} \nA média das notas é {m}')
    print('Você tirou a nota D')
    print('Reprovado')
elif m > 6 and m <= 7.5:
    print(f'A suas duas notas são {n1} e {n2} \nA média das notas é {m}')
    print('Você tirou a nota C')
    print('APROVADO')
elif m > 7.5 and m <= 9:
    print(f'A suas duas notas são {n1} e {n2} \nA média das notas é {m}')
    print('Você tirou a nota B')
    print('APROVADO')
elif m <= 10 and m > 9:
    print(f'A suas duas notas são {n1} e {n2} \nA média das notas é {m}')
    print('Você tirou a nota A')
    print('APROVADO')
else:
    print('Valor Inválido')
