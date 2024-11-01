quant = int(input('Quer inserir quantos Nomes? '))

arquivo = open('names.txt', 'w')
for n in range(quant):
    arquivo.write(input(f'Digite o {n+1}º Nome: ').title())
    arquivo.write('\n')
arquivo.close()
names = []
arquivo = open('names.txt', 'r')
for n in arquivo:
    names.append(n.strip())
arquivo.close()
names.sort()
arquivo = open('names.txt', 'w')
for n in range(len(names)):
    arquivo.write(f'{names[n]} \n')
arquivo.close()
