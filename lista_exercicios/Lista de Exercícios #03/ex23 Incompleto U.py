#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
nuPrim = []
n = int(input('Digite um número: '))
nrep = n
for j in range(nrep):
    prim = 0
    for i in range(1, n  + 1):
        if n % 1 == 0:
            prim += 1
    if prim == 2:
        print('Primo')
        nuPrim.append(n)
        print(n)
    nrep -= 1
print(nuPrim)
