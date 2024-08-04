ano = int(input('DIgite algum ano: '))
if ano%4 == 0 and ano != 100 or ano%400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
