soma = 0
cont = 0
for c in range(1, 7):
    nuber = int(input('ME DIGA O {}º VALORES:'.format(c)))
    if nuber % 2 == 0:
        soma = soma + nuber
        cont += 1
print('VOCÊ INFORMOU {} NÚMEROS E A SOMA FOI {}'.format(cont, soma))