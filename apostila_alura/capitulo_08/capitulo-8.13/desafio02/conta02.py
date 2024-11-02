class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def info(self):
        print(f'''Nome: {self.nome}
Sobrenome: {self.sobrenome}
CPF: {self.cpf}''')
        

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.year = year
        match month:

            case 1:
                month = 'Janeiro'
            case 2:
                month = 'Fevereiro'
            case 3:
                month = 'Março'
            case 4:
                month = 'Abril'
            case 5:
                month = 'Maio'
            case 6:
                month = 'Junho'
            case 7:
                month = 'Julho'
            case 8:
                month = 'Agosto'
            case 9:
                month = 'Setembro'
            case 10:
                month = 'Outubro'
            case 11:
                month = 'Novembro'
            case 12:
                month = 'Dezembro'

            case _:
                print('\033[32mERRO\033[m')
        self.month = month


class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura):
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
