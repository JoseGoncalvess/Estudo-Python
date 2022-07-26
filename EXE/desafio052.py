number = int(input('EM QUAL NUMERO VOCÊ ESTÁ PENSSANDO ?'))
tot = 0
for c in range(1, number + 1):
    if number % c == 0:
        print('\033[34m', end= ' ')
        tot = tot + 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO NUMERI {} FOI DIVISÍVEL {} VEZES '.format(number, tot), end = '')
if tot == 2:
    print('VEJA SÓ {} ELE É UM NÚMERO PRIMO'.format(number))
else:
    print('POR ISSO O NÚMERO {} NÃO É PRIMO'.format(number))