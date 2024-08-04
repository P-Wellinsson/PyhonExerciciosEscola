#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
pess = int(input('São quantas pessoas na turma? '))
s = 0
for i in range(1, pess + 1):
    age = int(input(f'Qual a idade da {i}º pessoa? '))
    while age > 180 or age < 0:
        age = int(input(f'\nA idade tem que ser maior ou igual a 1 ou menor que 180 \nQual a idade da {i}º pessoa? '))
    s += age
med = s / i
if med <= 25:
    fase = 'Jovem'
elif med <= 60:
    fase = 'Adulta'
else:
    fase = 'Idosa'
print(f'A média da turma é de {med}, portanto a turma é {fase}')
