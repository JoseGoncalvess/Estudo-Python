# DECLARAÇÃO DE VARIAVEIS
inicio = 0
fim = 100
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim+1):
    if numero % 5 == 0:
        print(numero)
# #LIST [ 0
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55
# 60
# 65
# 70
# 75
# 80
# 85
# 90
# 95
# #100]
# QUESTÃO DOIS
inicio = 100
fim = 500
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim+1):
    if numero % 2 == 0 and numero % 5 == 0 and numero % 7 == 0:

        print(numero)
# list[0
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55
# 60
# 65
# 70
# 75
# 80
# 85
# 90
# 95
# 100
# 140
# 210
# 280
# 350
# 420
# 490]
# QUESTÃO 3
inicio = 0
fim = 1000
divisor = 6
# verifica quais números são divisíveis por dividor, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % divisor == 0:
        print(numero)
# QUESTÃO 4
# variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'
print(nome.upper(), cidade.upper
      ())
print(nome.lower(), cidade.lower())
print(nome.find('ã'), cidade.find('ã'))
print(len(nome), len(cidade), len(cpf))

# mwtodo para retirar determandaos caracateres dentro de uma string percoror a string retirando os caracteres e juntando as partes
caracteres = ".-"
cpf = ''.join(x for x in cpf if x not in caracteres)
print(cpf)

# QUESTÃO 5
numero = '127957'
soma = 0
for x in range(0, len(numero)):

    soma = soma+int(numero[x])
print(soma)
a = True and False
b = False or True
print(a, b)
print(int(numero)+1.0)
