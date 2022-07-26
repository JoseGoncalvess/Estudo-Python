print('=====DESAFIO0042=====')
print()
print('BEM VIDO A SEMPRE BEM, VAMOS ANALISAR SEU IMC!?')
print()
print()
nome = (input('QUAL É O SEU NOME?'))
altura = float(input('QUAL É O SEU ALTURA ATUAL?'))
peso = float((input('QUAL É O SEU PESO ATUAL ?')))
imc = peso / (altura * altura)
print()
print('O RESULTADO DO SEU IMC É:')
if imc <= 18.5:
    print('{} ,CUIDADO!. VOCÊ SE ENCONTRA ABAIXO DO PESO'.format(nome))
elif 18.5 >= imc <= 24.5:
    print('{}, VOCÊ SE ENCONTRA PESO NORMAL'.format(nome))
elif 25 >= imc <= 29.9:
    print('{}, VOCÊ SE ENCONTRA EM SOBREPESO'.format(nome))
elif 35 >= imc <= 39.9:
    print('{}, VOCÊ SE ENCONTRA EM OBESIDADE GRAU 2'.format(nome))
else:
    print('{}, MUITO CUIDADO VOCÊ SE ENCONTRA EM OBESIDADE GRAU 3'.format(nome))

