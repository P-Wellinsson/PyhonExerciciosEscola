from conta02 import Cliente, Data, Conta
from datetime import date


cliente = Cliente('Pedro', 'Wellinsson', 1234-567-89)
data = Data(date.today().day, date.today().month, date.today().year)
conta = Conta('123-4', cliente, 10.0, 120.0, data)

conta.extrato()
