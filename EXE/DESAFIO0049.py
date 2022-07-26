print('=-'*10, 'TABUADA GROSSA', '-='*10)
tab = int(input('QUAL TABUADA DESEJA CONSULTAR?'))
print('-='*20)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(tab, c, tab*c))
print('-=' * 20)
print('{:=^20}'.format('CUIDA VAI ESTUDAR!'))