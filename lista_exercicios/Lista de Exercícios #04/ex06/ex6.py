from erro06 import *
aluno = {}
turma = []
respostas = 'V', 'F', 'V', 'V', 'F', 'V', 'F', 'F', 'V', 'F'

for a in range(1, 41):  # 40 alunos
    aluno['Nome'] = erroStr(f'Nome do {a} aluno: ')
    aluno['Nota'] = 0
    for i in range(10):
        respost = erroResp(
            f'{i+1}º Resposta de {aluno["Nome"]}: [V/F]', respostas[i])
        if respost:
            aluno['Nota'] += 1
    #print(aluno['Nota'])
    turma.append(aluno.copy())
    print('-' * 40)
#print(turma)
s = 0
for alun in turma:
    s += alun['Nota']
    for k, v in alun.items():
        print(f'{k}: {v}')
    print('-' * 40)
print(f'A média da turma é {s/40}')
