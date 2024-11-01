import random
def craps():
    ac = 1
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma = dado1+dado2
    h = soma
    print('A soma dos dados da primeira rodada foi:',soma, '\n')
    if soma == 11 or soma == 7:
       print('Voce ganhou!')
  
    elif soma == 2 or soma == 3 or soma == 12:
       print('Você perdeu!')
    
    else:
       while True:
           ac = ac + 1
           dado1 = random.randint(1,6)
           dado2 = random.randint(1,6)
           soma = dado1+dado2
           print(f'A soma dos dados da rodada {ac}° foi:',soma, '\n')
           if soma == 7:
              print('Voce perdeu!')
              break
      
           elif soma == h:
               print('Você ganhou')
               break
      
  
  
  

input('Aperte qualquer tecla para jogar:')
craps()
