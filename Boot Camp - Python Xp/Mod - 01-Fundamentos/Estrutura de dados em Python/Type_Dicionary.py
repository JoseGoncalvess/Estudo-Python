#DICIONARIO CRIADO
D1={'NOME':'BOB', 'IDADE':22, "CIDADE":'ARCOVERDE-PE'}
#ACESSO PELA CHAVE
print(D1['nome'.upper()])

#ADD ELEMENTOS A O DICIONÁRIO 
D2={'UM':1, 'DOIS':2, "TRES":3}
D2.update({'QUATRO':4,'CINCO':5})

print(D2)

#REMOVENDO ELEMENTOS DO DICIONÁRIO 
D2.pop('CINCO')
print(D2)


#INTERANDO COM O DICIONARIO
D3={'UM':1, 'DOIS':2, "TRES":3,"QUATRO":4,"CINCO":5,"SEIS":6}
#INTERANDO SOBRE AS CHAVES SEUEU DECLARO OU NÃO SMEPRE SERÁ SOBRE AS CHAVES
for key in D3:
    print(key, D3[key])

#DECLARADO
for key in D3.keys():
    print(key, D3[key])

#INTERANDO SOBR EOS VALORES
SOMA=0
for values in D3.values():
    SOMA= SOMA+values
print(SOMA)

#POSSO SOMAR APENAS USANDO  O METODO SUN
print(sum(D3.values()))
#MOSTRA OS VALORES COMO  UM OBJETO TIPO
print(D3.values())
#CONVERSAO EM LISTA DOS VALORES
print(list(D3.values()))

#INTERAÇÃO COM ITENS SEMPRE RETORNA UMA TUPLA
print(D3.items())

for ITEM in D3.items():
    print(ITEM)

#POSSO ADD UMA TUPLA COMO CHAVE = CHAVE COMPOSTA
D3.update({(3,5,6):'ESTÁ É UMA CHAVE COMPOSTA'})
print(D3)
print(D3[(3,5,6)])