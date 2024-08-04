from funções.erros import LeiaFloat

nota = []
for n in range(5):
    nota.append(LeiaFloat('Digite um número: '))
nota.sort()
del nota[0]
nota.pop()
print(f'A média da notas {nota} é {sum(nota)/3}')
