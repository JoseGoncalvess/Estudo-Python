import time
kgmax = 0
kgmin = 0
for peso in range(1,6):
    people = float(input('PESO DA {}º PESSOA ?'.format(peso)))
    if peso == 1:
        kgmax = people
        kgmin = people
    else:
        if people > kgmax:
            kgmax = people
        if people < kgmin:
            kgmin = people
time.sleep(1)
print('========= ANALIZANDO ==========')
time.sleep(1)
print('O MAIOR PESO IDENTIFICADO FOI {}kg'.format(kgmax))
print('E O MENOR PESO INDENTIFICADO FOI {}kg'.format(kgmin))