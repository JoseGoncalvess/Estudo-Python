import numpy as np 

#OPERAÇÃO DE SLOCE EM UMA RRAY
#ESTRUTURA 1D
A = [ 88, 19,86, 64,78]
a = np.array(A)
print(a.shape)

#ACESSANDO POR MEIO REVERSSO SO PASSAR O INDICES NEGATIVO
print(A[-1])


#ESTRUTURA 2D
B=[[10,21],[2,33],[44,8],[88,90]]
b = np.array(B)

#estrutura de slice retorna outro arrey
print(B[0:2])
print(b[1:2, 1:3])


X = np.linspace(start= 10, stop=100, num=10)
print('x', X)

#ACESSAR ELEMENTOS
print('ACESSAR 1º ELEMENTO', X[1])
print('ACESSAR 3º ELEMENTO', X[2])
print('ACESSAR ÚLTIMO ELEMENTO', X[9])
print('ACESSAR ÚLTIMO ELEMENTO', X[-1])


#ACESSAR  ELEMENTOS POR SLICES
print('ACESSAR 1ºs ELEMENTO', X[0:1])
print('ACESSAR 2ºs ELEMENTO', X[0:2])
print('ACESSAR 2ºs ELEMENTO', X[:2])


#GERANDO UM MATRIZ 2D
x = X.reshape(2,5)
print('x', x)

#ACESSAR 2d POR INDEX
print('ACESSAR 1º LINHA e 2º COLUNA', X[0:1])
print('ACESSAR 2º LINHA E PENULTIMA COLUNA', X[1:-4])
print('ACESSAR ULTIMA LINHA E ULTIMA COLUNA', X[1:4])


#ACESSAR 2d POR SLICES
print(x)
print('ACESSAR 1º LINHA INTEIRA', x[0:])
print('ACESSAR 1 LINHA 2ºE 4º COLUNA', x[1:2:4])
#PASSANDO O INDICE EM [-1] PARA PRESERVAR A ESTRUTURA DE COLUNA
print('ACESSAR ULTIMA COLUNA INTEIRA', x[:,[-1]])

#compartilhameto de memoria dos array
c = np.array([1,2,3])
print('c ANTES:', c)
d = c[:2]
print('d ANTES:', d)

#alteravalor em y muda o valor em x
d[0] = 200
print('c DEPOIS:', c)

#CASO NÃO QUEIRA QUE ALTERE USE A FUNÇÃO COPY()
c = np.array([1,2,3])
print('c ANTES:', c)
d = c[:2].copy()
print('d ANTES:', d)

#alteravalor em y NÃO muda o valor em x
d[0] = 200
print('d DEPOIS:', d)
print('c DEPOIS:', c)