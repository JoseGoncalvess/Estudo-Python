from datetime import date
print('=====DESAFIO0041=====')
print()
print()
print('=====COPA SECSU DE NATAÇÃO=====')
print()
print()
nome = str(input("OLÁ, COMO SE CHAMA ?"))
print('É UM PRAZER EM TE CONHECER {}, SEJÁ BEM VINDO A COPA SECSU DE NATAÇÃO!'.format(nome))
print('BOM, VAMOS DIRECIONAR  APARA SUA CATEGORIA:')
atual = date.today().year
ano = int(input('EM QUE ANO VOCÊ NASCEU?'))
idade = atual - ano

if idade <= 9:
    print('A SUA CATEGORIA É MIRIN, BOA SORTE {}'.format(nome))
if 14 > idade <= 9:
    print('A SUA CATEGORIA É INFATIL, BOA SORTE {}'.format(nome))
elif 19 > idade >= 14:
    print('A SUA CATEGORIA É JUNIOR, BOA SORTE {}'.format(nome))
elif 19 <= idade <= 20:
    print('A SUA CATEGORIA É SÊNIOR, BOA SORTE {}'.format(nome))
else:
    print('A SUA CATEGORIA É MASTER, BOA SORTE {}'.format(nome))