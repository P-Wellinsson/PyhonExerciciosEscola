usu = input('Digite o seu nome de Usuário: ').strip()
sen = input('Digite a sua senha: ').strip()
while sen == usu:
    print('A senha não pode ser igual ao nome de Usuário! \nDigite novamente')
    usu = input('Digite o seu nome de Usuário: ').strip()
    sen = input('Digite a sua senha: ').strip()
