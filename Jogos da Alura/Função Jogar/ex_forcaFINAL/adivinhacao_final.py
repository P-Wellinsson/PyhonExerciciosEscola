def jogar():
    from random import randint

    imprime_mensagem_abertura()
    nivel = int(input('Defina o nível: '))
    total_de_tentativas = defini_nivel(nivel)

    pontos = 1000
    random = randint(0,99)

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute = int(input('Digite um numero entre 0 e 99 '))
        print('Você digitou: ', chute)
        acertou = random == chute
        maior = chute > random
        menor = chute < random
        if (acertou):
            imprime_mensagem_vencedor()
            break
        else:
            pontos_perdidos = abs(random - chute)
            pontos -= pontos_perdidos
            if (maior):
                print('Você errou! O seu chute foi maior que o número secreto')
            elif (menor):
                print('Você errou! O seu chute foi menor que o número secreto')

    print('\033[34mFim do jogo!')
    print(f'Sua pontuação final é: {pontos}')
    print(f'O número secreto é {random}\033[m')


def imprime_mensagem_abertura():
    print('***************************************')
    print('***Bem vindo ao jogo da Adivinhação!***')
    print('***************************************')
    print('Escolha o nível de dificuldade:')
    print('(1) Fácil (20 tentativas)')
    print('(2) Médio (10 tentativas)')
    print('(3) Difícil (5 tentativas)')


def defini_nivel(nivel):
    while True:
        if nivel == 1:
            total_de_tentativas = 20
            break
        elif nivel == 2:
            total_de_tentativas = 10
            break
        elif nivel == 3:
            total_de_tentativas = 5
            break
        else:
            print('\033[31mDigite um número válido\033[m')
            nivel = int(input('Defina o nível: '))
    return total_de_tentativas


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
