n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
if n1 < n2 > n3:
    print(f'Na ordem decrescente é: \n{n1} \n{n2} \n{n3} ')
elif n3 > n2 > n1:
    print(f'Na ordem decrescente é: \n{n3} \n{n2} \n{n1} ')
elif n2 > n1 > n3:
    print(f'Na ordem decrescente é: \n{n2} \n{n1} \n{n3} ')
elif n3 > n1 > n2:
    print(f'Na ordem decrescente é: \n{n3} \n{n1} \n{n2} ')
elif n1 > n3 > n2:
    print(f'Na ordem decrescente é: \n{n1} \n{n3} \n{n2}')
elif n2 > n3 > n1:
    print(f'Na ordem decrescente é: \n{n2} \n{n3} \n{n1}')
elif n3 > n1 and n1 == n2:
    print(f'Na ordem decrescente é: \n{n3} \n{n1} \n{n2}')
elif n2 > n1 == n3:
    print(f'Na ordem decrescente é: \n{n2} \n{n3} \n{n1}')
elif n1 > n2 == n3:
    print(f'Na ordem decrescente é: \n{n1} \n{n3} \n{n2}')
elif n3 < n1 and n1 == n2:
    print(f'Na ordem decrescente é: \n{n1} \n{n2} \n{n3}')
elif n2 < n1 == n3:
    print(f'Na ordem decrescente é: \n{n1} \n{n3} \n{n2}')
elif n1 < n2 == n3:
    print(f'Na ordem decrescente é: \n{n2} \n{n3} \n{n1}')
else:
    print(f'Na ordem decrescente é: \n{n1} \n{n3} \n{n2}')
