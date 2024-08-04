numbers = []
for i in range(1, 11):
    numbers.append(int(input(f'Digite o {i}º número: ')))
n = int(input('\nDigite um número para eu dizer se está na lista: '))
if n in numbers:
    print(f'\033[34mO número {n} está na lista!\033[m')
else:
    print(f'\033[31mO número {n} não está na lista!\033[m')
