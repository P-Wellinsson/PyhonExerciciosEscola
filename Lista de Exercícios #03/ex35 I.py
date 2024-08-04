'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.
Para finalizar a votação digite "FIM"'''

c1 = c2 = c3 = c4 = vnul = vbranc = 0
while True:
    voto = input('''Existem 4 candidatos para essa eleição.
(0) Voto Nulo
(1) Pedro W.
(2) Rosilda B.
(3) George W.
(4) Cícera C.
(5) Voto em branco
 ''').strip()
    
    if voto == '0':
        vnul += 1
        print(' nulo ')
    elif voto == '5':
        vbranc += 1
        print(' branco ')
    elif voto == '1':
        c1 += 1
        print(' Pedro ')
    elif voto == '2':
        c2 += 1
        print(' Rosilda ')
    elif voto == '3':
        c3 += 1
        print(' George ')
    elif voto == '4':
        c4 += 1
        print(' Cícera ')
    else:
        print('\nValor inválido! \n')
    if voto in ('012345'):
        voto = True
    '''while True:
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
        if resp in('SN'):
            break
    if resp == 'N' and voto == True:
        break'''#Complicado
    
tot = c1 + c2 + c3 + c4
print(f'Candidato 1: {c1} votos \nCandidato 2: {c2} votos \nCandidato 3: {c3} votos \nCandidato 4: {c4} votos \n{vnul} votos nulos \n{vbranc} votos em branco. ')
