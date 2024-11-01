def erroStr(msg):
    while True:
        try:
            result = input(msg)
        except (KeyboardInterrupt, IndexError):
            print('\033[31mDigite algo.\033[m')
        except Exception as erro:
            print(f'Erro {erro.__class__}')
        else:
            # print(f'Tudo Certo! {result}')
            return result


def erroResp(msg, r):
    while True:
        try:
            result = erroStr(msg).upper()[0]
        except IndexError:
            print('\033[31mDigite algo.\033[m')
            continue
        if result in ('VF'):
            #print('Verificando...')#
            if result == r:
                #print('Acertou!')#
                return True
            else:
                #print('\033[31mErrou\033[m')#
                return False
        else:
            print(f'\033[31mDigite apenas V ou F.\033[m')
