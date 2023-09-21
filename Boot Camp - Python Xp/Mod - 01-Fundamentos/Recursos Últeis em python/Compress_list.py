#COMPRESSÃO DE LISTAS EM PYTHON

#LISTA COMPRESS
##LIST=[expert for expert in range]
#/
#/
#LISTA COMPRESS CONDICIONAL
##LIST=[expert for expert in range if()]

#CRIANDO LISTA D E1  10 ELEVADO A 2
lista=[]
for item in range(1,11):
    lista.append(item**2)
print(f'A LISTA COM FOR FICA ASSIM {lista}')

#MESMA FUNÇÃO ESCRITA DE MANEIRA PYTONICA
#POTENCIA
POTENCIA = [i**2 for i in range(1,11)]
print(f'A LISTA PYTONICA FICA ASSIM {POTENCIA}')

#MULTIPILICAÇÃO
multiplica = [i*10 for i in range(1,11)]
print(f'A LISTA DE MULTIPLICAÇÃO {multiplica}')

#CARACTERES EMMAIUSCULOS
CARACTERES = [c.upper() for c in 'Paralelepipeto']
print(f'A LISTA DE CARARACTERES MAIUSC. {CARACTERES}')

#RESTO ZERO
#EXEMPLO D ELISTA CONDICIONADA
LISTPAR = [(c %2 ==0) for c in range(1,11)]
print(f'A LISTA DE NUMEROS PARES {LISTPAR}')

#LISTA IMPAR 
LISTIMPA=[]
for item in range(1,11):
    if(item % 2 !=0):
        LISTIMPA.append(item**2)
print(f'A LISTA DE NUMEROS IMPARES {LISTIMPA}')

#LISTA IMPAR COM CONDIÇAO
LISTPAR = [o **2 for o in range(1,11) if(o % 2 !=0)]
print(f'A LISTA DE NUMEROS IMPARES {LISTPAR}')