from funções.erros import LeiaStr

frase = LeiaStr('Digite uma frase: ').split(' ')
print(f'Há {len(frase)} palavras na frase.')
