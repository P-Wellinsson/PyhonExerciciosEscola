fat = int(input('Digite um número inteiro para ser o fatorial: '))
while fat < 0:
    fat = int(input('Não existe fatorial negativo! \nDigite um número inteiro para ser o fatorial: '))
tot = 1
print(f'{fat}!', end=' = ')
for i in range(1, fat + 1):
    print(fat, end='')
    tot *= fat
    fat -= 1
    print(' . ' if fat != 0 else ' = ', end='')
print(tot)
