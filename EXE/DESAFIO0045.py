from random import randint
from time import sleep
print('{:=^60}'.format('DESAFIO0045'))
itens = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
j1 = int(input('QUAL A SUA JOGADA ?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!!')
print('-='* 10)
print('MAQUINA JOGOU {}'.format(itens[computador]))
print('VOCE JOGOU {}'.format(itens[j1]))
if computador == 0: #pedraa
    if j1 == 0:
        print('EMPATE')
    if j1 == 1:
        print('VOCÊ GANHOU')
    if j1 == 2:
        print('MAQUINA GANHOU')

elif computador == 1:#papel
    if j1 == 0:
        print('VOCÊ PERDEU')
    if j1 == 1:
        print('EMPATE')
    if j1 == 2:
        print('VOCÊ GANHOU')

elif computador == 2:#tesoura
    if j1 == 0:
        print('VOCÊ GANHOU')
    if j1 == 1:
        print('MAQUINA GANHOU')
    if j1 == 2:
        print('EMPATE')

else:
    print('{:=^40}'.format('JOGADA INVALIDADA'))


