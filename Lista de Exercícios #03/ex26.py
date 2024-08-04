# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
from time import sleep
c1 = c2 = c3 = 0
eleitor = int(input('Quantidade de eleitores: '))
for n in range(1, eleitor + 1):
    while True:
        voto = int(input('''\nEm quem você quer votar?
Candidato 1: Pedro Wellinsson
Candidato 2: George Weeubc
Candidata 3: Rosilda Bezz

Em quem quer votar? Digite (1) (2) ou (3) de acordo com o candidato: \n'''))
        if voto == 1:
            c1 += 1
            break
        elif voto == 2:
            c2 += 1
            break
        elif voto == 3:
            c3 += 1
            break
        else:
            print(
                f'Número {voto} não está entre os candidatos, digite novamente: ')
            sleep(4.3)

print(
    f'O candidato 1 teve {c1} votos \nO candidato 2 teve {c2} votos \nE a candidata 3 teve {c3} votos')
