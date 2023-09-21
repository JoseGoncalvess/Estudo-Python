# CONDIÇÕES EM PYTHON
# ======== CARTEIRA DE HABILITAÇÃO==========
# PESSOAS
vitor = 22
ana = 16
glauber = 52
p = glauber

# TESTE DE HABILITAÇÃO
if(p > 18 and p < 50):
    {
        print(f'{p} Está Apto para prosseguir com o Teste de habilitação')
    }
elif(p < 18):
    {
        print(f'{p} Não Está Apto para prosseguir com o Teste de habilitação')}

else:
    {
        print(f'{p}Você esta buscadno atualizar sua habilitação')

    }
# ESTRUTURA DE REPETIÇÃO
# while basease em condição
cont = 0
while cont <= 10:

    cont = cont + 1
    print(cont)
print()

# CASO DO FOR
# for basease em sequencia d ealguam coisa ( percorrer)
n = 10
coisa = 20+1
for n in range(coisa):
    soma = n+1
    print(soma)
