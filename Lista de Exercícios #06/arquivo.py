arquivo = open('texto.txt', 'w')
arquivo.write('Abobora\n')
arquivo.write('Cenoura \nLimão \nBatata frita \n')
arquivo.close()

arquivo = open('texto.txt', 'a')
arquivo.write('couve \n')
arquivo.close()

listcomp = []
arquivo = open('texto.txt', 'r')
for line in arquivo:
    listcomp.append(line.strip())
# print(listcomp)
arquivo.close()
listcomp.append('sabão')

arquivo = open('texto.txt', 'w')
for produt in listcomp:
    arquivo.write(produt+'\n')
arquivo.close()
arquivo = open('texto.txt', 'a')
arquivo.write('panetone')
arquivo.close()
