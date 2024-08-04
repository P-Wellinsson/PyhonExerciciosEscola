b = int(input('Digite a base do número: '))
ex = int(input('Digite o expoente do número: '))
p = 1
for i in range(ex):
    p *= b
print(f'A base {b} elevada ao expoente {ex} é igual á {p}')
