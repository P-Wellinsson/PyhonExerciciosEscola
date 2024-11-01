'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$1.000,00; Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual deste funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''
sal = 1000.00
perc = 1.5
sal1y = sal + sal * (perc/100)
perc *= 2
salfim = sal1y * 2
print(sal, sal1y, perc, salfim)
