# Implemente uma função que remove os elementos duplicados de uma lista.
def remove_duplicata(lista):
    list_fin = []
    for element in lista:
        if element not in list_fin:
            list_fin.append(element)
    return list_fin


lista = ['processador', 'memoria', 'teclado', 'monitor', 'webcam', 'impressora', 'software', 'hardware', 'mouse', 'usb', 'internet', 'rede', 'tablete', 'servidor', 'router', 'sistema', 'windows', 'laptop', 'linux', 'firewall', 'antivirus', 'navegador', 'banco', 'dados', 'arquivos', 'memoria', 'cpu', 'placa', 'video', 'webcam', 'microfone',
         'celular', 'tablete', 'notebook', 'laptop', 'configuracao', 'codigo', 'memoria']
# memoria, webcam, laptop, tablete
lista_fim = remove_duplicata(lista)
print(f'Retirando as palavras duplicadas ficam: {lista_fim}')
