class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def info(self):
        print(f'''Nome: {self.nome}
Sobrenome: {self.sobrenome}
CPF: {self.cpf}''')


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou:
            destino.deposita(valor)
            return True
        else:
            return False

    def extrato(self):
        print(f'número: {self.numero}')
        self.titular.info()
        print(f'saldo: {self.saldo}')
