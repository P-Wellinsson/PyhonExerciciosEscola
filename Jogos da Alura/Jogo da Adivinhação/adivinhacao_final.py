from random import randint

print('Escolha o nível de dificuldade:')
print('(1) Fácil (20 tentativas)')
print('(2) Médio (10 tentativas)')
print('(3) Difícil (5 tentativas)')
nivel = int(input('Defina o nível: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

pontos = 1000

random = randint(0,99)

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite um numero entre 0 e 99 '))
    print('Você digitou: ', chute)
    acertou = random == chute
    maior = chute > random
    menor = chute < random
    if (acertou):
        print('Você acertou!')
        break
    else:
        pontos_perdidos = abs(random - chute)
        pontos -= pontos_perdidos
        if (maior):
            print('Você errou! O seu chute foi maior que o número secreto')
        elif (menor):
            print('Você errou! O seu chute foi menor que o número secreto')

print('Fim do jogo!')
print('Sua pontuação final é: {}'.format(pontos))
