def jogar():
    from random import randrange

    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')

    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra? ")

        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[posicao] = letra
                posicao = posicao + 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!!')
    else:
        print('Você perdeu!!')
    print('Fim do jogo')
