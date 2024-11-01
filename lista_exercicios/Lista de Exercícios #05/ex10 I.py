'''Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador
lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada,
você tirar 7 ou 11, você é um "natural" e ganhou. Se você tirar 2, 3 ou 12 na
primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira
jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo
agora é continuar jogando os dados até tirar este número novamente. Você
perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.'''


def game():
    round1 = False
    while True:
        win = False
        value = int(input('Digite o valor dos dados: '))
        if value in (4,5,6,8,9,10):
            if round1:
                if value == ponto:
                    win = True

            else:
                round1 = True
                ponto = value
                continue
        elif value in (7,11):
            win = True
            print('venceu') #Tirar
        elif value in (2,3,12):
            win = False
            print('não venceu') #Tirar
        else:
            print('\033[31mDigite um número válido.\033[m')
            continue
        print(value, win, round1)


game()
