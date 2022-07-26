nomevelho = ''
maiorage = 0
medage = 0
somaag = 0
famele = 0
for a in range(1,6):
    print('------- {}º Pessoa-------'.format(a))
    name = str(input('NOME:')).strip()
    age = int(input('IDADE:'))
    gen = str(input('sexo [M/F] ?')).upper()
    somaag += age
    if a == 1 and gen == 'M':
        maiorage = name
        nomevelho = name
    if gen == 'm' and age > maiorage:
        maiorage = age
        nomevelho = name
    if gen == 'F' and age < 20:
        famele += 1
medage = somaag / 4
print("A MEDIA DA IDADE DO GRUPO É DE {} ANOS".format(medage))
print('O HOMEM VAI VELHO DO GRUPO TEM {} ANOS E SE CHAMA {}'.format(nomevelho, maiorage))
print('AO TODO SÃO {} MULHERES COM MENOS DE 20 ANOIS'.format(famele))


