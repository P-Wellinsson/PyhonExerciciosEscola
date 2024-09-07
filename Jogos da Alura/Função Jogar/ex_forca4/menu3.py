import adivinhacao
import ex_forca4.forca1a as forca

print(33 * '*')
print('**********MENU DE JOGOS**********')
print(33 * '*')
print('''1) Adivinhação
2) Forca''')
escolha = int(input('Qual jogo quer jogar? Digite o número: '))

if escolha == 1:
    adivinhacao.jogar()
elif escolha == 2:
    forca.jogar()
