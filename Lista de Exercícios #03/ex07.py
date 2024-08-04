mn = 0
for n in range(5):
    n = float(input('Digite um número: '))
    mn = mn * 0 + n if mn < n else mn
print(f'O maior número é o número {mn}')
