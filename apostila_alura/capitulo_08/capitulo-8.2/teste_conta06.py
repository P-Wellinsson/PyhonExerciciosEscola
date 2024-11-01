def cria_conta(numero, titular, saldo, limite):
    """
    Ele cria a conta, Tendo como parâmetro número, titular, saldo e limite.
    Cria um dicionário com o número, titular, saldo e limite.
    return: dicionário
    """
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(f'número: {conta["numero"]} \nsaldo: {conta["saldo"]}')


conta = cria_conta('123-7', 'João', 500.0, 1000.0)
deposita(conta, 50.0)
extrato(conta)

saca(conta, 20.0)
extrato(conta)

help(cria_conta)