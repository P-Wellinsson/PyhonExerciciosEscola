class Conta:
    def __init__(self, titular, numero, saldo, limite):
        print("inicializando uma conta...")
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print(self.saldo)


conta = Conta('123-4', 'João', 500, 2000.0, )
depos = float(input('Depositador: '))
conta.deposita(depos)
conta.extrato()
