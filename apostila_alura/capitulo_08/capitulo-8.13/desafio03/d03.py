from conta03 import *  # Cliente, Conta , historico

historico = Historico()
cliente1 = Cliente('Pedro', 'Wellinsson', '1234-567-89')
cliente2 = Cliente('Jean', 'Malungis', '987-654-321-82')
conta1 = Conta('123-4', cliente1, 10.0, 120.0)
conta2 = Conta('9743-3', cliente2, 3500000.0, 12000000.0)

conta2.deposita(10000.0)
conta2.saca(5000.0)
conta2.transfere_para(conta1, 200.0)
conta2.extrato()

conta1.historico.imprime()
conta2.historico.imprime()
