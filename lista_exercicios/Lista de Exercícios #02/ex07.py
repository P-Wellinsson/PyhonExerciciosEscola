n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior ')
elif n2 > n3 and n2 > n1:
    print(f'O número {n2} é o maior ')
elif n3 > n1 and n3 > n2:
    print(f'O número {n3} é o maior ')
else:
    print('Dois ou maiores números são iguais')
if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o menor')
elif n2 < n3 and n2 < n1:
    print(f'O número {n2} é o menor ')
elif n3 < n1 and n3 < n2:
    print(f'O número {n3} é o menor ')
else:
    print('Dois ou mais números são iguais. ')
