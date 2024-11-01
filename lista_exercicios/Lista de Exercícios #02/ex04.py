l = input('Digite uma letra: ').upper()
if len(l) > 1:
    print('Digite uma única letra ')
elif l in 'AEIOU':
    print(f'A letra {l} é uma vogal ')
elif l in 'BCDFGHJKLMNPQRSTVWXYZ':
    print(f'A letra {l} é uma consoante ')
else:
    print('Digite uma única letra')
