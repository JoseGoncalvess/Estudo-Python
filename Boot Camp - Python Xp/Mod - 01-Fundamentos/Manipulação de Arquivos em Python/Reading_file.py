#criando uma leitura de arquivos

#LEIURA DE TODAS A AS LINHAS D EUMA SO VEZ
aq= open('Boot Camp - Python Xp\Mod - 01/Manipulação de Arquivos em Python/file/city.txt','r')
linha = aq.read()
aq.close()
print(linha)

#LEIURA LINHA  LINHA, RETORNANDO UMA LISTA DE STRINGS
aq= open('Boot Camp - Python Xp\Mod - 01/Manipulação de Arquivos em Python/file/city.txt','r')
linhas = aq.readlines()
aq.close()
print(linhas)

#MANIPULANDO LINAHS
new_line=[]
for linha in linhas:
    new_line.append(linha.rstrip())
    print(new_line)



#INTERAR SOBRE CADA LINHA NO ARQUIVO 
aq= open('Boot Camp - Python Xp\Mod - 01/Manipulação de Arquivos em Python/file/city.txt','r')
for linha in aq:
    print(linha.rstrip())
aq.close()


#MANIPULANDO OUTRAS SITUAÇÃO DE SOMA
aq= open('Boot Camp - Python Xp\Mod - 01/Manipulação de Arquivos em Python/file/city.txt','r')
soma=0
for linha in aq:
    cidades = linha.split(' ')
    populacao= int(cidades[-1])
    soma = soma + populacao
aq.close()
print(f'A soma da populaçãoé :{soma}')
