#1. Faça um programa que escreve uma frase digitada pelo usuário em um arquivo. Em seguida, o programa deve ler e imprimir o conteúdo desse arquivo.
frase = input('Digite uma frase: ')
arquivo = open('frase.txt', 'w')
arquivo.write(frase)
arquivo.close()
arquivo = open('frase.txt', 'r')
print(arquivo.readline())
