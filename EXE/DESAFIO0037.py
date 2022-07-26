import time
nuber = int(input('DIGITE UM NÚMERO A SER CONVERTIDO:'))
print('''ESCOLHA UMA DA OPÇÕES DE CONVERSSÃO
[1]BINARIO
[2]OCTAL
[3]HEXADECIMAL''')
options = int(input('SUAS OPÇÕES:'))
time.sleep(1)
print('{=*20}', 'CONVERTENDO','{=*20}')
time.sleep(1)
if options == 1:
    print('{} CONVERTIDO PARA BINÁRIO É IGUAL {}'.format(nuber, bin(nuber)[2:]))
elif options == 2:
    print('{} CONVERTIDO PARA OCTAL É {}'.format(nuber, oct(nuber)[2:]))
elif options == 3:
    print('{} CONVERTIDO PRA HEXADECIMAL É {}'.format(nuber, hex(nuber)[2:]))
else:
    print('OPÇÃO INVALIDA, POR FAVOR ESCOLHAA OPÇÃO CORRETA')