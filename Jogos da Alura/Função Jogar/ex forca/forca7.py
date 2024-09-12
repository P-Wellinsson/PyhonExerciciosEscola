print(33 * '*') # Moisés e Pedro
print('***Bem vindo ao jogo da Forca!***')
print(33 * '*')
palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']

acertou = False
enforcou = False
erros = 0
while not acertou and not enforcou:
    chute = input('Qual letra? ')
    posicao = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[posicao] = letra
        posicao += 1
