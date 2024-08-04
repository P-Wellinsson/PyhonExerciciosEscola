from funções.erros import *

nums = []
while True:
    n = LeiaInt('Digite um número: ')
    if not n in nums:
        nums.append(n)
    else:
        print('\033[31mJá existe esse número.\033[m')
    while True:
        resp = input(f'Quer continuar? [S/N] ').upper()
        if resp == 'S' or resp == 'N':
            break
        else:
            print('\033[31mDigite apenas S ou N. \033[m')
    if resp == 'N':
        break
print(
    f'Em ordem crescente fica {sorted(nums)} \nEm ordem decrescente fica {sorted(nums, reverse=True)}')
