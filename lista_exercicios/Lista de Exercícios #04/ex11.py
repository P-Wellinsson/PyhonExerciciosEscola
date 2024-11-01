from funções.erros import LeiaStr

frase = LeiaStr('Digite uma frase: ').replace(' ', '').upper()
frase2 = ''.join(reversed(frase))
if frase2 == frase:
    print(f'\033[32mA frase é um palíndromo.\033[m')
else:
    print(f'\033[33mA frase não é um palíndromo.\033[m')
