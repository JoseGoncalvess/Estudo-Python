#DLECAANDO UMA FUNÇÃO E PYTHON

L1=[0,1,2,3,4,5,6,7,8,]
L2=[0,11,2,88,]
L3=[3,55,5,6,7,]

#CRIANDO UMA FUNÇÃO DE SOMA
SOMA=0
def SOMA_LISTA(Lista):
    for item in Lista:
        result=SOMA+item
    return result


print(SOMA_LISTA(L1))
print(SOMA_LISTA(L2))
print(SOMA_LISTA(L3))