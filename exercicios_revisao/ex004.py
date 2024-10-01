# Faça um programa que conte a frequência de cada palavra em uma frase.

frase = input('Digite uma frase: ').strip() .lower() .split(' ')
words = {}
for word in frase:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# Não está funcionando corretamente por causa dos caracteres especiais como '.', ',', '*', etc...
