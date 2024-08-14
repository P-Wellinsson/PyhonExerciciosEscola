n = int(input('Você quer ler quantos nomes? '))
arquivo = open('names.txt', 'w')
for a in range(n):
    name = input('Digite um nome: ')
arquivo.close()
arquivo = open('names.txt', 'r')
