while True:
    tot = c = 0
    produts = []
    while True:
        prod = float(input('\nPreço da mercadoria: R$'))
        while prod < 0:
            prod = float(input('\nPreço Inválido!! \nPreço da mercadoria: R$'))
        if prod == 0:
            break
        tot += prod
        c += 1
        produts.append(prod)
    print(f'\nPreço total: R${tot:.2f}')
    money = float(input('Valor a ser pago: R$'))
    while money < tot:
        money = float(input('O valor a ser pago tem que ser maior que o valor total! \nValor a ser pago: R$'))

    print('\nLojas Tabajara')
    for i in range(1, c + 1):
        print(f'Produto {i}: R$ {produts[i-1]:.2f}')
    print(f'''Total: R$ {tot:.2f}
Dinheiro: R$ {money:.2f}
Troco: R$ {money - tot:.2f}''')
