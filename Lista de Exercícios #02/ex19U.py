n = int(input('Digite um número inteiro menor que 1000: '))#27
if 1000 < n < 1:
    print('Número inválido!!! \nDigite um número menor que 1000 ou maior que 0!')

u = n % 10
d = (n % 100) // 10
c = n // 100
uFi = f'{u} unidade' if u == 1 else f'{u} unidades'
dFi = f'{d} dezena' if d == 1 else f'{d} dezenas'
cFi = f'{c} centena' if c == 1 else f'{c} centenas'

print(f'{cFi}, {dFi} e {uFi}')
