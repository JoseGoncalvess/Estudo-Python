print('======DESAFIO0038======')
print()
print()
print('VAMOS COMAPARA NUMEROS!')
a = input('me diga um número !')
b = input('me diga outro número !')
print()
print()
print()
print('=====.....analisando.....=====')
print()
print()
if a < b or b > a:
    print('{} é o maior!'.format(b))
elif a > b or b < a:
    print('{} é o maior!'.format(a))
elif a == b:
    print('não a valor maior, ambos são iguais!')