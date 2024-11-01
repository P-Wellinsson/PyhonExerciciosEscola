from funções.erros import *

lista = [4, 5, 34, 655, 32, 78, 53, 400, 45, 35, 6, 2, 44, 55]
ab = []
a = LeiaInt('Digite um número (A): ')
b = LeiaInt('Digite um número (B): ')
if a <= b:
    for c in range(a+1, b):
        ab.append(c)
else:
    for c in range(b+1, a):
        ab.append(c)
cont = 0
for l in lista:
    if l in ab:
        cont += 1


print(f'Tiveram {cont} números que estavam na lista e no intervalo fechado')
