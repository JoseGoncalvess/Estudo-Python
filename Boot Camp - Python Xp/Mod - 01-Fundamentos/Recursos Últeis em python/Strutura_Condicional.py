#APLICANDO ESTRUTURA CONDICIONAL EM UMA LINHA

# ATRIBUINDO D EMANEIRA CONDICIONAL
NOME = 'ANNY'

if(len(NOME)>3):
    var = 100
else:
    var =len(NOME)
print(f'Se nome atribuiu o valor {var} a Variavel')


#ATRIBUIDO CONDIÇÃO EM UMA LINHA 
NAME = 'JU'
#O ELSE PRECISA SER DECLARADNO NESSE CASO DE ATRIBUIÇÃO
var = 100 if len(NAME) <4 else 0
print(f'Se nome CONDICIONAL Astribuiu o valor {var} a Variavel')
