repeat = 'S'
while repeat == 'S':
    apo = int(input('Quanto é a população da cidade "A"? '))
    acres = float(input('Quais as taxas de crescimento iniciais da cidade "A"? '))
    bpo = int(input('Quanto é a população da cidade "B"? '))
    bcres = float(input('Quais as taxas de crescimento inicias da cidade "B"? '))
    year = 0
    while apo <= bpo:
        apo += apo * (acres/100)
        bpo += bpo * (bcres/100)
        year += 1
    print(f'Vai demorar {year} anos para a cidade "A" ultrapassar a cidade "B". ')
    repeat = input('Você quer repetir a operação? \n[S/N]').upper()
    while not repeat in ('SsNn') or len(repeat) != 1:
        print(f'Valor {repeat} incorreto!!')
        repeat = input('Você quer repetir a operação? \n[S/N] \n').upper()
if repeat == 'N' or repeat == 'n':
    print(' \nFinalizado com sucesso!! ')
