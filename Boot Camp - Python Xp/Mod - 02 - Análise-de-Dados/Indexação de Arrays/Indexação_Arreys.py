import numpy as np

#Indexação Array 1D
lista= [1,2,3,4,5,66]
A= np.array(lista[-1])
print(A)

array = [[1234],[5678],[9,10,11]]
B = np.array(array)
#passo o indiece da LINHA e COLUNA
print(B[2,3])

# na quesão de Slice, passo o intervalo
B[1:3, 2:3]
