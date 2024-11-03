class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def info(self):
        print(f'''\n\033[34mNome:      \033[44m{self.nome}\033[m
\033[34mSobrenome: \033[44m{self.sobrenome}\033[m
\033[34mCPF:       \033[44m{self.cpf}\033[m \n''')
        

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

    def info(self):
        # print(f'{self.day} de {self.month} de {self.year}')
        return f'\033[35m{self.day} de {self.month} de {self.year}.\033[m'


class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = str(saldo).replace('.', ',')
        self.limite = limite
        self.data_abertura = data_abertura

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
        print(f'\033[34mNúmero:    \033[44m{self.numero}\033[m')
        self.titular.info()
        print(f'\033[34mSaldo:     \033[44m{self.saldo}\033[m')
    
    def abertura(self):
        print(f'A data de abertura é {self.data_abertura.info()}')
