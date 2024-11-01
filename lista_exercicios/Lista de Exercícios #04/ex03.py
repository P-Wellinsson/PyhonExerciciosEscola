numbers = []
pos = neg = 0
for i in range(10):
    numbers.append(int(input(f'Digite o {i+1}º número: ')))
    if numbers[i] >= 0:
        pos += 1
    else:
        neg += 1
print(f'''A média dos números é {sum(numbers)/i:.2f}
O maior valor foi {max(numbers)} e o menor foi {min(numbers)}
Foram {pos} elementos positivos e {neg} negativos''')
