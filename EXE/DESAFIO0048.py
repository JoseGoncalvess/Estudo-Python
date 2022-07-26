#ACOMULEITOR
soma = 0
#CONTER
cont = 0
#FUNCTION
for c in range(1, 501, 2):
    ##SABER SE O NUMERO É DIVIDOR POR 3
    if c % 3 == 0:
        soma = soma + c
        cont = cont +1
print('A somas dos {} valores solicitadois é {}'.format(cont, soma))
