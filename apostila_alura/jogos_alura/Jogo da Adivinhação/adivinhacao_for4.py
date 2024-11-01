numero_secreto = 42
pontos = 1000
nivel = int(input('Qual o nível? [1;2;3]: '))
if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite o seu número: '))
    pontos -= abs(numero_secreto - chute)
    if pontos <= 0:
        print('\033[31mVocê teve a capacidade de zerar a pontuação, seu Bananão de chocolate\033[m')
        break
    print('Você digitou: ', chute)
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if acertou:
        print('Você acertou!')
        break
    elif maior:
        print('Você errou! O seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou! O seu chute foi menor que o número secreto')
print('\033[35mFim do jogo!\033[m')