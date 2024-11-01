a = 80000
b = 200000
year = 0
while a <= b:
    a += a * (3/100)
    b += b * (1.5/100)
    year += 1
print(f' vai demorar {year} anos para a população do país "A" ultrapassar a do país "B" ')
