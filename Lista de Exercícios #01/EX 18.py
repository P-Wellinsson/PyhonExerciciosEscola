mb = float(input('Qual é o tamanho do arquivo em MB? '))
mbps = float(input('Existem quantos mbps? '))
d = (mb /mbps) /60
print(f'O tempo aproximado de download do arquivo é de {d} minutos')
