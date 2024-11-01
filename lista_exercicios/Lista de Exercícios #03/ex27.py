s = 0
turm = int(input('Qual é a quantidade de turmas? '))

for i in range(1, turm + 1):
    alun = int(input(f'Qual é a quantidade de alunos na {i}ª turma? '))
    while alun > 40 or alun < 1:
        alun = int(input(
            f'\nTem que ter no minímo 1 aluno e no máximo 40 \nQual é a quantidade de alunos na {i}ª turma? '))
    s += alun
print(f'A média de alunos por turma é de {s/i}')
