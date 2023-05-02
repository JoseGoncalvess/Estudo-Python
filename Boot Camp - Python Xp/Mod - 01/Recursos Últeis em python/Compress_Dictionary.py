#COMPRESSÃO DE DICIONARIO 
#COMPRESS DICIONARIO
##{CHAVE: VALOR for ITEM in SEQUENCI}

#COMPRESS DICIONARIO COM CONDIÇÃO
##{CHAVE: VALOR for ITEM in SEQUENCI}

#ULTILIZANDO O METODO FOR
dic_1={}
for item in range(1,11):
    dic_1[item] = item**2
print(f'Assim ficou o dicionario {dic_1}')


#ULTILIZANDO O METODO COMPRESS
dic_2={ B : B ** 2 for B in range(1,11)}
print(f'Assim ficou o dicionario DE B {dic_2}')


#NUMEROS IMPARES
dic_IMAPR={}
for item in range(1,11):
    if(item % 2 !=0):
        dic_IMAPR[item] = item**2
print(f'Assim ficou o dicionario IMPAR : {dic_IMAPR}')

#ULTILIZANDO O METODO COMPRESS
dic_PAR={ B : B ** 2 for B in range(1,11) if (B % 2 == 0)}
print(f'Assim ficou o dicionario IMPAR DE  B {dic_PAR}')