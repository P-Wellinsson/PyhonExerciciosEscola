impar = []
par = []
allImp = []
allPar = []
while True:
    try:
        n = int(input('Digite um número [0 finaliza]: '))
    except ValueError:
        print('\033[31mDigite um número válido\033[m')
        continue
    except KeyboardInterrupt:
        print('\n\033[31mEscolha um número! \033[m')
        continue
    if n % 2 == 0:
        par.append(n)
        allPar.append(n)
    else:
        impar.append(n)
        allImp.append(n)
    if n == 0:
        break
    if len(par) == 5:
        print(par)
        par = []
    if len(impar) == 5:
        print(impar)
        impar = []
print(f'Os pares foram {allPar}. \nOs impares foram {allImp}.')
