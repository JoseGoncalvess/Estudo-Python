print('=====DESAFIO0044=====')

print('{:=^80}'.format('PAG E LEVE'))

comp = float(input('QUAL O VALOR DASUA COMPRA?'))
print('''
[1] AVISTA CHEQUE OU DINHEIRO OU PIX')
[2] AVISTA CARTÃO
[3] 2X NO CARTÃO
[4]  3X OU MAIS NO CARTÃO''')
fpag = int(input('QUAL A FORMA DE PAGAMENTO ?'))

cod1 = comp - (comp * 10 / 100)
cod2 = (comp - (comp * 5 / 100))
cod3 = comp / 2
if fpag == 1:
    print('SUA COMPRA NO VALOR DE R${}, FICAR POR {}'.format(comp, cod1))

elif fpag == 2:
    print('SUA COMPRA NO VALOR DE R${}, FICAR POR {}'.format(comp, cod2))
    print()
    print('{:=^50}'.format('RETIRE SEU CARTÃO, TRANSAÇÃO ACEITA!'))

elif fpag == 3:
    print('SUA COMPRA NO VALOR DE R${}, FICAR POR {}'.format(comp, cod3))
    print()
    print('{:=^50}'.format('RETIRE SEU CARTÃO, TRANSAÇÃO ACEITA!'))

elif fpag == 4:
    nubf = int(input('EM QUANTAS VEZES QUER DIVIDIR ?'))
    cod4 = (comp / nubf) + 20 / 100
    print('SUA COMPRA NO VALOR DE R${}, FICAR POR {}'.format(comp, cod4))
    print()
    print('{:=^50}'.format('RETIRE SEU CARTÃO, TRANSAÇÃO ACEITA!'))
else:
    print('PARA PROSSEGUIR ESCOLHA A FORMA D EPAGAMENTO!')
    print('{:=^40}'.format('TENTE NOVAMENTE'))
