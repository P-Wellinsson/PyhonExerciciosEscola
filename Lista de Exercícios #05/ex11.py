# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def data(d, m, a):
    val = True
    if a >= 0 and 12 >= m > 0 and 0 < d <= 31:
        if m in (1, 3, 5, 7, 8, 10, 12):
            if d <= 31:
                val = True
            else:
                val = False
        elif m in (4, 6, 9, 11):
            if d <= 30:
                val = True
            else:
                val = False
        else:  # Ano Fevereiro, 28 ou 29. Depende se é bissexto
            if d == 29 and a % 4 == 0 and a != 100 or a % 400 == 0:
                val = True
            elif d <= 28:
                val = True
            else:
                val = False
    else:
        val = False

    if val == False:
        return 'NULL'
    else:
        if m == 1:
            m = 'Janeiro'
        elif m == 2:
            m = 'Fevereiro'
        elif m == 3:
            m = 'Março'
        elif m == 4:
            m = 'Abril'
        elif m == 5:
            m = 'Maio'
        elif m == 6:
            m = 'Junho'
        elif m == 7:
            m = 'Julho'
        elif m == 8:
            m = 'Agosto'
        elif m == 9:
            m = 'setembro'
        elif m == 10:
            m = 'Outubro'
        elif m == 11:
            m = 'Novembro'
        else:
            m = 'Dezembro'
    return f'{d} de {m} de {a}'


print('-=' * 30)
print(f'{"Digite abaixo uma Data no formato DD/MM/AAAA".center(60)}')
print('-=' * 30)
d = int(input('Digite o Dia: '))
m = int(input('Digite um mês: '))
a = int(input('Digite um ano: '))
print(data(d, m, a))
