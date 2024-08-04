from time import sleep
sim = 0

print('Vou te fazer 5 perguntas sobre o crime')
sleep(2)
p1 = input('Você telefonou para a vítima? \nSim ou Não? ').strip() .upper()
p2 = input('Você esteve no local do crime? \nSim ou Não? ').strip() .upper()
p3 = input('Mora perto da vitíma? \nSim ou Não? ').strip() .upper()
p4 = input('Você devia para a vitíma? \nSim ou Não? ').strip() .upper()
p5 = input('ULTIMA PERGUNTA, você já trabalhou com a vitíma? \nSim ou Não? ').strip() .upper()

if p1 == 'SIM':
    sim = sim + 1
if p2 == 'SIM':
    sim = sim + 1
if p3 == 'SIM':
    sim = sim + 1
if p4 == 'SIM':
    sim = sim + 1
if p5 == 'SIM':
    sim = sim + 1

if sim == 2:
    print('Você está classificada como SUSPEITA')
elif sim == 5:
    print('Você é o ASSASSINO!!!')
elif sim >= 3:
    print('Você está classificada como CÚMPLICE')
else:
    print('INOCENTE!')
