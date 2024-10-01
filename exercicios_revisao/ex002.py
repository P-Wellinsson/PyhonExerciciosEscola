# Faça uma função que recebe uma lista e retorna uma nova lista com os elementos invertidos.
def inversao(num):
    num.reverse()
    return num


list = ['processador', 'memoria', 'teclado', 'monitor', 'impressora', 'software', 'hardware', 'mouse', 'usb', 'internet', 'rede', 'servidor', 'router', 'sistema', 'windows', 'linux', 'firewall', 'antivirus', 'navegador', 'banco', 'dados', 'arquivos', 'memoria', 'cpu', 'placa', 'video', 'webcam', 'microfone',
        'celular', 'tablete', 'notebook', 'laptop', 'configuracao', 'codigo', 'programa', 'compilador', 'debug', 'memoria', 'ssd', 'hd', 'armazenamento', 'backup', 'criptografia', 'login', 'senha', 'registro', 'cache', 'driver', 'atualizacao', 'upload', 'download', 'bit', 'byte', 'terabyte', 'gigabyte', 'processo', 'serial']

nun = [1, 2, 13, 4, 5, 7, 8, 10]

print(f'A inversão dos números é {inversao(nun)}\n')
print(f'A inversão da lista "\033[36mlist\033[m" é {inversao(list)}')
