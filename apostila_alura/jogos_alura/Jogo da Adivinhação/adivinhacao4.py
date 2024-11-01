print(56 * '*')
print('*       Jogo da adivinhação Do Pedro e do Daniel       *')
print(56 * '*')

numero_secreto = 42

chute = input('Digite o seu número: ')
print(f'Você digitou: {chute}')

if numero_secreto == chute:
    print('Você acertou!')
else:
    print('Você errou!')