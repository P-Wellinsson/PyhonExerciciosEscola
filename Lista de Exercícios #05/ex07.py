'''Faça um programa que use a função valorPagamento para determinar o valor a
ser pago por uma prestação de uma conta. O programa deverá solicitar ao
usuário o valor da prestação e o número de dias em atraso e passar estes
valores para a função valorPagamento, que calculará o valor a ser pago e
devolverá este valor ao programa que a chamou. O programa deverá então exibir
o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir
outro valor de prestação e assim continuar até que seja informado um valor
igual a zero para a prestação. Neste momento o programa deverá ser encerrado,
exibindo o relatório do dia, que conterá a quantidade e o valor total de
prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte
forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver
atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

def valorPagamento(Prestaçao, DAtraso):
    if DAtraso == 0:
        ValTot = Prestaçao
    else:
        ValTot = Prestaçao + (Prestaçao * (3/100)) + (Prestaçao * ((DAtraso * 0.1) /100))
    return ValTot


q = 0
VTot = 0
while True:
    VPrest = float(input('Digite o valor da prestação R$'))
    if VPrest == 0:
        break
    DAtras = int(input('Digite os dias de atraso: '))
    result = valorPagamento(VPrest, DAtras)
    q += 1
    VTot += result
    print(f'A prestação é de R${result:.2f}')

print(f'''{"-=" * 15}
{"Relatorio do dia".center(30)}
{"-=" * 15}
Quantidade: {q}
Valor total: R${VTot:.2f}''')
