primo = []
n = int(input('Digite um número: '))
while n <= 1:
    n = int(input('O número tem que ser maior que 1 \nDigite um número: '))
nalt = n

while nalt != 0:
    prim = 0
    for i in range(1, n): #Colocar (1, n + 1) se for de 1 até (n).
        if nalt % i == 0:
            prim += 1
    if prim == 2:
        primo.append(nalt)
    nalt -= 1
primo.sort(key=int)
print(f'Os números primos entre 1 e {n} são {primo}')
