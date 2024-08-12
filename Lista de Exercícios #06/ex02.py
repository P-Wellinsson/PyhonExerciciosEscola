arquivo = open('chamada.txt', 'w')
arquivo.write('1234567 Brunilde \n')
arquivo.write('4636574 Josefina \n')
arquivo.write('9876234 Cleiton \n')
arquivo.write('9864356 Irineu \n')
arquivo.write('9074564 José \n')
arquivo.close()

galera = {}
turma = []

arquivo = open('chamada.txt', 'r')  # .replace()
for i in arquivo:
    gal = i.strip().split(' ')
    galera = {gal[0]: gal[1]}
    turma.append(galera)
print(f'As pessoas no dicionário são: ')
for c, dic in enumerate(turma):
    for k, v in dic.items():
        print(f'\033[35m{v}\033[m tem o ID: \033[32m{k}\033[m')
