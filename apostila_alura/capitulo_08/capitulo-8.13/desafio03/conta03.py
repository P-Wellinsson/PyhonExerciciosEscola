class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def info(self):
        print(f'''\033[34mNome:      \033[44m{self.nome}\033[m
\033[34mSobrenome: \033[44m{self.sobrenome}\033[m
\033[34mCPF:       \033[44m{self.cpf}\033[m ''')


class Historico:
    def __init__(self):
        from datetime import datetime
        self.data_abertura = datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'\033[35mData de Abertura: {self.data_abertura}\033[m')
        print('\033[33mTransações: \033[m')
        for t in self.transacoes:
            print(f'\033[31m- {t}\033[m')


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'depósito de R${valor}')

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.transacoes.append(f'Saque de R${valor}')
        else:
            return False

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'Transferência de R${valor} para conta {destino.numero}')

    def extrato(self):
        print(f'\033[34mNúmero:    \033[44m{self.numero}\033[m')
        self.titular.info()
        print(f'\033[34mSaldo:     \033[44m{str(self.saldo).replace(".", ",")}\033[m \n')
        self.historico.transacoes.append(f'Tirou extrato - saldo de R${self.saldo}')
