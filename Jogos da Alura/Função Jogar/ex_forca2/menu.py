import adivinhacao
import ex_forca3.forca1 as forca1

print(33 * '*')
print('**********MENU DE JOGOS**********')
print(33 * '*')
print('''1) Adivinhação
2) Forca''')
escolha = int(input('Qual jogo quer jogar? Digite o número: '))

if escolha == 1:
    adivinhacao.jogar()
elif escolha == 2:
    forca1.jogar()
