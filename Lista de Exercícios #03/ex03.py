name = input('Qual é o seu nome? ').strip()
while len(name) <= 3:
    name = input('Informação Inválida!! \nQual o seu nome? ').strip()

age = int(input('\nQual é a sua idade? '))
while age < 0 or age > 150:
    age = int(input('Informação Inválida!! \nQual é a sua idade? '))

sal = float(input('\nQual é o seu sálario? R$'))
while sal <= 0:
    sal = float(input('Informação Inválida!! \nQual é o seu sálario? R$'))

sex = input('\nQual é o seu sexo [M/F] ').strip()
while not sex in ('MmFf') or len(sex) != 1:
    sex = input('Informação Inválida!! \nQual é o seu sexo [M/F] ').strip()

civ = input('\nQual é o seu estado Cívil? ').strip().upper()
while not civ in ('SVCD') or len(civ) != 1:
    civ = input('Informação Inválida!! \nQual é o seu estado Cívil? ').strip().upper()
print('\nTudo válido! ')
