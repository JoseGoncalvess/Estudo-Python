from datetime import date
corrent_year = date.today().year
totalmax = 0
totalmini = 0
for people in range(1, 8):
    nasc = int(input('EM QUE ANO A {}º PESSOA NASCEU ?'.format(people)))

    age = corrent_year - nasc
    if age >= 21:
        totalmax += 1
    else:
        totalmini += 1
print('AO TODO TIVEMOS {} PESSAO MAIORES DE IDADE!'.format(totalmax))
print('E TAMBÉM TIVERMOS {} PESSOAS MENORES DE IDADE!'.format(totalmini))