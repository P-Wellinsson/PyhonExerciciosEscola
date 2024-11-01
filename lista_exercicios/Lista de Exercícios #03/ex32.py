tabu = int(input('Tabuada do número: '))
inic = int(input('Comecar por: '))
fim = int(input('Terminar em: '))
while fim < inic:
    inic = int(input('\nO final Tem que ser maior que o começo \nComecar por: '))
    fim = int(input('Terminar em: '))
mult = inic
all = inic * tabu
for i in range(inic, fim + 1):
    print(f'{tabu} X {mult} = {all}')
    mult += 1
    all += tabu
print('FIM')
