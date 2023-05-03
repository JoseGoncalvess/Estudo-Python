import Processalista
from Processalista import*
import Processalista as pl





#QUESTÃO 1- EXECUTAR O COD ABAIXO
# relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
# estrutura que irá armazenar o número de letras de cada nome
qtd_letras = {}
# calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
for nome in nomes:
 qtd_letras[nome] = len(nome)

print(qtd_letras) #// {'Maria': 5, 'Julieta': 7, 'Fernando': 8, 'Cristiano': 9, 'Cláudio': 7}

#Questãod a ativdade
print(type(nomes))
print(type(qtd_letras))

#qustão da atividade
print(len(nomes))
print(len(qtd_letras))



#QUESTÃO 2 - RELAIXAR DICIONARIA COMPRESSE BASEADO NO COD ANTERIOR
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
qtd_letras={ nome:len(nome) for nome in nomes}
print(qtd_letras) #// {'Maria': 5, 'Julieta': 7, 'Fernando': 8, 'Cristiano': 9, 'Cláudio': 7}

#QUETÃO 3 -CALCULANDO A AREA DO CIRCULO PASSADNO OS PARAMETROS 
#MODELO - A
PI=3.14
def ARE_CIRCULO_A(Raio):
    return PI*(Raio**2)
print(ARE_CIRCULO_A(8))#//200.96

#MODELO-B
def ARE_CIRCULO_B(Raio,pi):
    return pi*(Raio**2)
print(ARE_CIRCULO_B(8, 3.15))#/200.96


#QUESTÃO - 5- REESCREVENDO FUNÇÃO AREA ULTILIZANOD LAMBDA
PI=3.14
CALC_AREA_CIRCULO = lambda Raio: PI*(Raio**2)
print(CALC_AREA_CIRCULO(3))#/28.26


#QUESTÃO - 6 - VERIFICÇÃO DE DISPONIBILIDADE DE HORARIO MEDICO
# relação de dias da semana que cada médico atende
cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}
# Calcula quais os dias possíveis para dois médicos

def disp_dois_especialistas(medico01, medico02):
    disponibilde = (medico01&medico02)
    return F'o DIA DISPONIVEL PARA ATENDIMENTO É: {disponibilde}'
print(disp_dois_especialistas(cardiologista, dermatologista))
 # <seu codigo aqui>
# Calcula quais os dias possíveis para três médicos
def disp_tres_especialistas(medico01, medico02, medico03):
    diponibilide = (medico01&medico02)|(medico01&medico03)|(medico02&medico03)
    return F'OS DIAS DISPONIVEIS PARA ATENDIMENTO SÃO: {diponibilide }'
print(disp_tres_especialistas(cardiologista, ortopedista, neurologista))





