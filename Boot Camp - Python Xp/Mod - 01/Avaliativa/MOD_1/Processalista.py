# Encontra e retorna o maior número impar presente na lista

lista_nuber = [1,2,4,6,8,9,99,33,5,17]
#RETORA MAIOR NUBER IMPAR DA LISTA
def maior_impar(lista):
    list_impar=[ number for number in lista_nuber if(number %2 !=0)]
    maior_number= list_impar[0]
    for item  in list_impar:
        if item > maior_number:
            maior_number= item
    return  maior_number

#RETORA MAIOR NUBER IMPAR DA LISTA
def menor_impar(lista):
    list_impar=[ number for number in lista_nuber if(number %2 !=0)]
    menor_number = list_impar[0]
    for item  in list_impar:
        if item < menor_number:
            menor_number= item
    return  menor_number


def numeros_impares(LISTA):
    maior= maior_impar(LISTA)
    menor= menor_impar(LISTA)
    return ( F'o MAIOR NUMERO IMPAR DA LISTA É: {maior}, E O MENOR: {menor}')

print( numeros_impares(lista_nuber))
            


    
       


       
            



#  # <seu codigo aqui>
# # Encontra e retorna o menor número impar presente na lista
# def menor_impar(lista):
#  # <seu codigo aqui>
# # Encontra e retorna o maior e o menor número ímpar presentes na lista
# def menor_impar(lista):
#  # <seu codigo aqui>