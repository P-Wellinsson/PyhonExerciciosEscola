#Faça um programa que calcule e mostre a média aritmética de N notas.
s = c = 0
while True:
    while True:
        n = float(input('Digite uma nota de 0 á 10: '))
        if 0 <= n <= 10:
            break
    s += n
    c += 1
    while True:
        rep = input('Quer continuar? [S/N]').strip().upper()[0]
        if rep in('SN'):
            break
    if rep == 'N':
        break
print(f'A média de {c} notas é {s/c:.2f}')
