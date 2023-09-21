import numpy as np 
#Array - estrutur de manipulação de dados numericos em form de vetores e matrizes
#numpy - estremamente rapido comparado ao python puro
#comando para saber sobre um importe

# print( help(np.array(object)))

#CRIAÇÃO DE ARRAY 1D
lista=[1,2,3,4]
x = np.array(lista)
print(f'X: {x}')
print(x.shape)


#CRIAÇÃO DE ARRAY 2D
lista=[[1,2],[2,3],[4,8]]
x = np.array(lista)
print(f'X\n:{x}')
print(x.shape)

#arrey cintendo apenas 0
dim = (2,2)#(linhas, coluna)
x = np.array(lista)
x= np.zeros(dim)
print(f'X\n:{x}')
print(x.shape)


#atribuido um arrey por meio de intervalos
minx, maxx= 1,50
x= np.linspace(minx, maxx, num=50)
print(f'X\n:{x}')
print(x.shape)

#criação de matiz identidade
num=5
x= np.eye(num)
print(f'X\n:{x}')
print(x.shape)

#criação de valorez aleatorios

x= np.random.random(size=(2,2))#(linha, coluna)
print(f'X\n:{x}')
print(x.shape)
