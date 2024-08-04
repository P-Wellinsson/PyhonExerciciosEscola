#5. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
#A função “altera” o valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto/100) + custo
    return imposto


imposto = float(input('Quantidade de imposto: '))
preço = float(input('Preço do item R$'))
TotPreco = somaImposto(imposto, preço)
print(f'O imposto sobre vendas é de R${TotPreco:.2f}')
