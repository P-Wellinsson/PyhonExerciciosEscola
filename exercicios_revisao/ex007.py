# Faça uma função que verifica se um número é primo.
def num_primo(n):
    """Verifica se um número é ou não um número primo.
    se ele for um número primo 
    return: True
    se ele não for um número primo
    return: False"""
    if n == 1:
        return False
    for i in range(2, n):
        if n / i == n // i:
            return False
    return True


n = int(input('Digite um número inteiro: '))
if num_primo(n):
    print(f'\033[32mO número {n} é um número primo.\033[m')
else:
    print(f'\033[31mO número {n} não é um número primo.\033[m')
