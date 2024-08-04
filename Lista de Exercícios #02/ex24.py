'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
oper = input('Digite qual operação deseja realizar: Soma, Subtração, Multiplicação ou Divisão \n').strip() .upper()

if oper == 'SOMA':
    n = n1 + n2
    nPI = f'é par,' if n% 2 ==0 else f'é impar,'
    nPN = f'positivo,' if n >= 0 else f'negativo,'
    nID = f'e inteiro.' if n/1 == n//1 else f'e decimal.'
    print(f'O número {n} {nPI} {nPN} {nID}')

elif oper == 'SUBTRAÇÃO':
    n = n1 - n2
    nPI = f'é par,' if n% 2 ==0 else f'é impar,'
    nPN = f'positivo,' if n >= 0 else f'negativo,'
    nID = f'e inteiro.' if n/1 == n//1 else f'e decimal.'
    print(f'O número {n} {nPI} {nPN} {nID}')

elif oper == 'MULTIPLICAÇÃO':
    n = n1 * n2
    nPI = f'é par,' if n% 2 ==0 else f'é impar,'
    nPN = f'positivo,' if n >= 0 else f'negativo,'
    nID = f'e inteiro.' if n/1 == n//1 else f'e decimal.'
    print(f'O número {n} {nPI} {nPN} {nID}')

elif oper == 'DIVISÃO':
    n = n1 / n2
    nPI = f'é par,' if n% 2 ==0 else f'é impar,'
    nPN = f'positivo,' if n >= 0 else f'negativo,'
    nID = f'e inteiro.' if n/1 == n//1 else f'e decimal.'
    print(f'O número {n} {nPI} {nPN} {nID}')
else:
    print('Valor INVÁLIDO!!')
