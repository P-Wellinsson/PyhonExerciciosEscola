# Crie uma lista com os números de 1 a 100 e imprima os números pares.
nums = []
for i in range(1, 101):
    nums.append(i)
par = []
for n in nums:
    if n % 2 == 0:
        par.append(n)
print(f'Os números pares são {par}')
