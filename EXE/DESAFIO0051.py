print('='*50)
print('{:^50}'.format('10 TERMOS DE UM PA'))
print('='*50)
primeiro = int(input('PRIMEIRO TERMO?'))
razao = int(input('QUAL A RAZÃO?'))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=" -> ")
print('THE END')
print('='* 30)
print('{:=^30}'.format('you like, the project ?'))
print('=' * 30)