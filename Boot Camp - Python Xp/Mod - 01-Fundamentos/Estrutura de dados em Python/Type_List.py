# LISTA
nuemro = [1, 2, 3, 4, 5, ]
# ACESSARA LISTA PELO INDICE
print(nuemro[0])
print(nuemro[3])
print(nuemro[1])
print(nuemro[4])
# ACESSARA LISTA PELO SLICE(SEQUENCIA)
print(nuemro[0:2])
print(nuemro[2:])
print(nuemro[-1:])
# COMPARAÇÃO DE IDADE
pesoa = [22, 15, 36]
pesoas = [22, 15, 36, 42, 88, 79, 45, 11,
          10, 36, 95, 55, 22, 0, 11, 2, 3, 6, 33]
maior_idade = pesoas[0]
for idade in pesoas:
    if idade > maior_idade:
        maior_idade = idade
print(maior_idade)


# OU POSSO USAR A PROPRIEDADES MAX
print(max(pesoas))
# ADD UM NEW VALUE THE LIST
pesoa = [22, 15, 36]
pesoa.append(999)
print(pesoa)
pesoa.remove(pesoa[0])
print(pesoa)
#FUNÇÕES DE OPERAÇÃO +,*,IN
l11 =[1,4,'a', 'y']
l12 =[none,true,'v', 'y']
print(l11+l12)#SOMO AS LISTAS
print(l12*2)#REPITO A LISTA XX
print(l11 in l12)#VERIFICO SE OS ELEMNETOS CONTEM DENTRO DA LISTA


# FUNÇÕES IMPORTANTE
num = [3, 2, 5, 9, 8, 4, 45, 36, 32]
print(len(num))  # QUANTIDADE D EELEMENTO DA LISTA
print(sum(num))  # SOMA OS ELEMENTOS DA LISTA
print(num.reverse)  # INVERTE  AORDEM DA LISTA
print(num.extend([2, 5, 88, 99, 6]))  # ADD ELEMENTOS  ALISTA JA EXISTENTE
print(num.sort())  # ORDENA A LSITA
# DEFINOA  APOSIÇÃO QUE QUERO COLOCAR DETERMIANDO ELEMENTO
print(num.insert(2, '555'))
print(num.pop())  # REMOVO O ULTIMO INTEMDA LISTA
print(num.clear())  # OLIMPA  ALISTA(EXCLUIR)
# RETORNA O VALOR DA POSIÇÃO QUE PASSEI EM SUA PRIMEIRA APARIÇÃO
num = [3, 2, 5, 9, 8, 4, 45, 36, 32]
print(num.index(45))# RETORNA A POSIÇÃO DO ELEMENTO DENTRO DA LISTA
print(num.count(4))  # RETORNA QUANTAS VEZES ESSE ELEMENT APARECEU NA LISTA
