# Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
num2 = num1 = 0
if n1 > n2:
    for nu2 in range(n2 + 1, n1):
        print(nu2, end=' ')
        num2 += nu2
    print(f'\nA soma dos números é {num2}')
elif n1 < n2:
    for nu1 in range(n1 + 1, n2):
        print(nu1, end=' ')
        num1 += nu1
    print(f'\nA soma dos números é {num1}')
else:
    print('Não existe nenhum número entre eles! ')
