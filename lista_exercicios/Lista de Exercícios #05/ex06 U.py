def conversao(hora, minuto):
    if hora < 0 or hora > 24 or minuto > 59 or minuto < 0:
        turno = 'ERRO'
    elif hora >= 13:
        hora -= 12
        turno = 'A'
    else:
        turno = 'P'
    tempo = [hora, minuto, turno]
    return tempo


def saida(hora, minuto, turno):
    if turno == 'ERRO':
        print('\033[31mERRO, O horário está errado!\033[m')
    else:
        print(f'{hora}:{minuto} {turno}.M.')


while True:
    hora = int(input('Digite a hora: '))
    minuts = int(input('Digite os minutos: '))
    convert = conversao(hora, minuts)
    saida(convert[0], convert[1], convert[2])
    while True:
        resp = input('Quer continuar? [S/N]: ').upper().strip()[0]
        if resp in ('SN'):
            break
    if resp == 'N':
        break
print(f'\033[32mObrigado pela Preferência. \033[m')
