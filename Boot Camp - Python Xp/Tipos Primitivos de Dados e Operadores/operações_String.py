# string
nome = ' consolação'
rua = 'rua '
art = ' da '
#print(rua + art+nome)

# Particulas 'in' e not'in"
# usase in para saber se estar em alguam coisa
a1 = ' consolação'
a2 = 'sol'
print(a1 in a2)
print('brasil' in a2)
print(a2 in a1)
print(a1 not in a2)

print(len(nome))


# METODO IMBUTIDOS
pais = 'brasil'
print(pais.upper())  # TODAS AS LETRASEM MAIUSCULO
print(pais.lower())  # TODAS AS LETRASEM MINUSCULO
print(pais.title())  # PRIMEIRA LEITRA MAISUCULO
# SUBISTITUI O PRIMEIRO ARGUMENTO PELO SEGUNDO
print(pais.replace('brasil', 'portugal'))
print(pais.startswith('brasil'))  # SE A STRING COMEÇA COM ESSA SUBSTRING
print(pais.endswith('brasil'))  # SE A STRING TERMINA COM ESSA SUBSTRING
print(pais.find('brasil'))  # MOSTRA ONDE CoMEÇA O INDEICE DESSA SUBSTRING

# SEPARA AS STRINGS POR DELIMITADOR EM ASPAS " " PASSO O DELIMITADOR
print(pais.split(' '))
