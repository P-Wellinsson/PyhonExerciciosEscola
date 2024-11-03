from conta02 import Cliente, Data, Conta
from datetime import date


cliente = Cliente('Jean', 'Malungis', '987-654-321-82')
data = Data(date.today().day, date.today().month, date.today().year)
conta = Conta('9743-3', cliente, 3500000.0, 12000000.0, data)

conta.extrato()
conta.abertura()
