# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''from random import shuffle
n = 'abastardela'
shuffle(n)
print(n)'''


def embaralha(string):
    from random import shuffle
    troca = []
    for i in string:
        troca.append(i)
    shuffle(troca)
    trocado = ''
    for i in troca:
        trocado += i
    return trocado.upper()


string = embaralha(input('Digite algo: '))
print(f'A palavra embaralhada é {string}')
