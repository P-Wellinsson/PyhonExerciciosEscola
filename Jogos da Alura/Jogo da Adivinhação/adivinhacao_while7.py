numero_secreto = 42
total_de_tentativas = 3
rodada = 1
while rodada <= total_de_tentativas:
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute_str = input('Digite o seu número: ')
    print(f'Você digitou: {chute_str}')

    acertou = chute_str == numero_secreto
    maior = chute_str > numero_secreto
    menor = chute_str < numero_secreto

    if acertou:
        print('Você acertou!')
        break
    elif maior:
        print('Você errou! O seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou! O seu chute foi menor que o número secreto')
    rodada += 1
print('Fim do jogo')