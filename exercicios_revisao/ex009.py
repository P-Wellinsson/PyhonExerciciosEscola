# Crie uma função que recebe uma lista de números e retorna a média, o maior e o menor valor.

def med_plus(lista):
    """Recebe uma lista numérica, podendo ser tanto int quanto float e retorna uma lista com a média, o maior e o menor número nesta ordem"""
    med = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)
    return [med, maior, menor]


nuns = [7, 43, 22, 37, 48, 28, 3, 32, 27]
lista = med_plus(nuns)
print(f'Os números {nuns} tem a média de {lista[0]:.2f}, o maior número é {lista[1]} e o menor é {lista[2]}')
