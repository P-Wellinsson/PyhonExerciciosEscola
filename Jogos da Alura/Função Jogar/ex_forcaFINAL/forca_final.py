from random import randrange
from arquivo_final import arq

def carrega_palavra_secreta():
    arq()
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print('Fim do jogo')


def imprime_mensagem_abertura():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def pede_chute():
    chute = input('Qual letra? ').strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1


def imprime_mensagem_vencedor():
    print('\033[32mParabéns, você ganhou!\033[m')
    print("       ___________     ")
    print("      '._==_==_=_.'    ")
    print("      .-\\:      /-.   ")
    print("     | (|:.     |) |   ")
    print("      '-|:.     |-'    ")
    print("        \\::.    /     ")
    print("         '::. .'       ")
    print("           ) (         ")
    print("         _.' '._       ")
    print("        '-------'      ")


def imprime_mensagem_perdedor(palavra_secreta):
    print('\033[31mPuxa, você foi enforcado!\033[m')
    print(f'A palavra era {palavra_secreta}')
    print("    _______________        ")
    print("   /                \       ")
    print("  /                  \      ")
    print("//                    \/\   ")
    print("\|   XXXX    XXXX     | /  ")
    print(" |   XXXX    XXXX     |/   ")
    print(" |   XXX      XXX     |    ")
    print(" |                    |    ")
    print(" \__      XXX       __/    ")
    print("   |\     XXX      /|      ")
    print("   | |            | |      ")
    print("   |  I I I I I I I |        ")
    print("   |  I I I I I I   |       ")
    print("   \_              _/       ")
    print("    \_           _/         ")
    print("       \_______/            ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
    elif erros == 2:
        print(" |      (_)   ")
        print(" |      \\     ")
    elif erros == 3:
        print(" |      (_)   ")
        print(" |      \\|    ")
    elif erros == 4:
        print(" |      (_)   ")
        print(" |      \\|/   ")
    elif erros == 5:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
    elif erros == 6:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")
    elif erros == 7:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()
