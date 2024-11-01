number = []
impar = []
par = []
p = i = 0
for c in range(10):
    number.append(int(input(f'Digite o {c+1} número: ')))
    if number[c] % 2 == 0:
        par.append(number[c])
        p += 1
    else:
        impar.append(number[c])
        i += 1
print(f'''Os números digitados foram {sorted(number)}
Tiveram {p} números  par(es) que foram {par}
Tiveram {i} números impar(es) que foram {impar}''')
