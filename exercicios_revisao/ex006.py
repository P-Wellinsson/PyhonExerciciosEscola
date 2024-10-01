# Crie uma função que calcula o fatorial de um número.
def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


n = int(input('Digite um número inteiro: '))
print(fatorial(n))
