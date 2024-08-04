#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def quant(n):
    return len(str(n))


n = quant(int(input('Digite um número inteiro: ')))
print(n)
