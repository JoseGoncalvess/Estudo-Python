print('=====DESAFIO0040=====')

print()
print('=======ESCOLA DA TITIA TETEIA====== ')
print()
not1 = int(input('QUAL A SUA PRIMEIRA NOTA ??'))
not2 = int(input('QUAL A SUA SEGUNDA NOTA ??'))
op = (not1 + not2) / 2
if op < 5.0:
    print('sua nota é:{}'.format(op))
    print('É meu querido você se fodeu!!')
if op <= 5.0 or op < 6.9:
    print('sua nota é:{}'.format(op))
    print(' você ainda tem chance!')
else:
    print('sua nota é:{}'.format(op))
    print('PARABÉNS AGORA VOCÊ É UM DESEMPREGADO!')
