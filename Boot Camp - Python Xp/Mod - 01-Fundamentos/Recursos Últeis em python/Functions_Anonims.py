# FUNÇÕES ANONIMAS OU LAMBDS
def AREA_QUADRADO (LADO):
    return LADO * LADO

print(f'Com a função normal {AREA_QUADRADO(4)}')

#DECLARAÇÃO DA FUNÇÃO LAMBDA
AREA_QUADRADO2 = lambda LADO : LADO*LADO
print(f' com a função lambda AREA_QUADRADO: {AREA_QUADRADO2(8)}')

#DECLARAÇÃO DA FUNÇÃO LAMBDA COM MAIS D  UM ARGUMENTO
AREA_TRIANGULO = lambda BASE, ALTURA : BASE*ALTURA
print(f' com a função lambda AREA_TRIANGULO:  {AREA_TRIANGULO(8,12)}')


#MAPEANDO UMA LISTA APLICANOD  UMA FUNÇÃO LAMBDA

TRIPLO = lambda X: X*3
LISTA = [1,2,3,4,5,6,7,8]
#com o metodo map percorro os item d alista aplicado a função a cada item 
print( list(map(TRIPLO, LISTA)))

#APLICANOD AO ESCOPOD DO MAP
print(list(map(lambda x: x**x, [1,2,4,5,6,7,8,9])))