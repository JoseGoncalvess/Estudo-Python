

sex= str(input(
          '''
========== Opções=========
[M] MASCULINO
[F] FEMININO
QUAL É O SEU SEXO?''').strip().upper()[0])
while sex not in 'MmFf':
    sex =(str(input('''FAVOR DIGITE  AOPÇÃO INDICADA [M/F]:
''').strip().upper()[0]))
print('SEXO {} REFISTRADO COM SUCESSO!'.format(sex))
