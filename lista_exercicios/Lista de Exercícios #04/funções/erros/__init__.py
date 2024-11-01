def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                f'\033[31mERRO: Por favor digite um número inteiro válido.\033[m')
            continue  # Volta pro while
        except KeyboardInterrupt:
            print(f'\033[31mDigite um valor.\033[m')
        else:
            return n


def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(
                f'\033[31mERRO: Por favor digite um número válido.\033[m')
            continue  # Volta pro while
        except KeyboardInterrupt:
            print(f'\033[31mDigite um valor.\033[m')
        else:
            return n


def LeiaStr(msg, nums=False):
    while True:
        try:
            n = input(msg).strip()
        except KeyboardInterrupt:
            print('\n\033[31mDigite algo.\033[m')
        except Exception as erro:
            print(erro.__class__)
        else:
            if n == '':
                print('f\033[31mDigite algo.\033[m')
                continue
            if nums == False:
                nums = True
                for l in n:
                    if l.isnumeric():
                        nums = False
                        break
            if nums:
                return n
            else:
                print('\033[31mDigite apenas palavras.\033[m')
                continue
