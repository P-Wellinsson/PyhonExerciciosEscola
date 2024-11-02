from conta14 import Conta

conta = Conta('123-4', 'João', 120.0, 1000.0)
print(conta.numero)
print(conta.titular)

conta2 = Conta('432-1', 'Pedro', 10.00000, 100)
conta2.deposita(15.0)
conta2.extrato()
conta2.saca(5.0)
conta2.extrato()
