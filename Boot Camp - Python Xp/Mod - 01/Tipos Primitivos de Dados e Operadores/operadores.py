# Operadores primitivos em python
# ANDA = E => "UME E O OUTRO TBM"
# OR = OU => "UME OU OUTRO "
# NOT = OCONTRARIO(NÃO) => "O CONTRARIO DAQUELA COISA "


# EX#############3

# COM AND
# ambos tem que ser valido para acontecer
bolo_de_laranja = False
bolo_de_mandioca = True
if(bolo_de_laranja and bolo_de_mandioca):
    {
        print('São otiams escolhas de bolo!')
    }
else:
    {
        print('Acho o bolo de laranja Melhor!')
    }
# COM OR
# pelomenos um deles deve ser valido pra acontecer
bolo_de_laranja = False
bolo_de_mandioca = True
if(bolo_de_laranja or bolo_de_mandioca):
    {
        print('São otiams escolhas de bolo!')
    }
else:
    {
        print('Acho o bolo de laranja Melhor!')
    }
# COM NOT
# define o contrario do outro
B = 2
A = -2
if(not A == B):
    {
        print('acho que deu certo!')
    }
else:
    {
        print('acho quedeu errado!')
    }

# USO DE VARIAVES NO MEIO DA EXPRESSSÃO
questoes = 200
Qacertos = 80

result = (Qacertos/questoes)*100  # forma um multiplicando depois
resulte = (Qacertos*100) / questoes  # resolvenod por regra de 3
print(f"Aporveitamento de {result}%")
print(f"Aporveitamento de {resulte:.2f}%")
