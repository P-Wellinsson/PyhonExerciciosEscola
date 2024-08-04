par = imp = 0
for n in range(1, 11):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        par += 1
    else:
        imp += 1
print(f'Foram {par} números pares e {imp} números impares')
