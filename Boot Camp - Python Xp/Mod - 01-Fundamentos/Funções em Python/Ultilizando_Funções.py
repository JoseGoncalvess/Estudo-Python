#ULTILIZAÇÃO D EFUNÇÕES D EMODO GERAL
def AREAQUA(LA, LB):
    RESULTADO = LA*LB
    return RESULTADO

def IMC(PESO, ALTURA):
    IMC =PESO/(ALTURA*ALTURA)
    return IMC

def WELCOME(NOME):
    print(f'WELCOME TO PROGRAMING WOLRD, {NOME}!')


#CHAMDO DAS FUNÇÕES
print(AREAQUA(10, 2))
print(IMC(88, 1.75))
print(WELCOME('GONÇALVES'))


#OUTROS CASOS D EFUNÇÃO COM MENSSAGEM DE ERRO
def DIV(DIV, DIVISOR):
    if DIVISOR ==0:
        return 'ERRO EM UMA DAS INFORMAÇÕES, REVEJA OS VALORES'
    
    DIVI = DIV/DIVISOR
    return DIVI

print(DIV(10, 2))
print(DIV(10, 0))

#RESULTADO COM MAIS DE UM VALOR 
def DIV2(DIV, DIVISOR):
    if DIVISOR ==0:
        return 'ERRO EM UMA DAS INFORMAÇÕES, REVEJA OS VALORES'
    
    DIVI = DIV/DIVISOR
    REST = DIV % DIVISOR
    return (DIVI, REST)

print(DIV2(10, 2))
print(DIV2(10, 0))

# atribuo variaves em sequencia e ele retorna respectivamente
divisor, resto = DIV2(10, 2)
print(divisor, resto)


#APROVEITANDO FUNÇÕES DENTRO DE OUTRAS
def validator(valor):
    if valor == 0:
        print("Valor não pode ser ultilizado, reveja os valores inseridos")
        return True
    return False
    
#VALIDANDO DETERMINADO DADO ANTES DE PORCESSEGUIR COM A ESTRUTURA POR MEIO D EUMA FUNÇÃO A PARTE
def calc(v1, v2):
    if validator(v2):
     return
    
    return v1 * v2

print(calc(3, 99))
print(calc(4, 0))


#ARGUMENTOS DE MANEIRA DECLARATIVA
def area(lado_a, lado_b):
    return lado_a*lado_b


print(area(30,3))

#FUNÇÃO COM VALORES PADRÃO DEFAUTH
def area(lado_a=2 , lado_b=0):
    return lado_a*lado_b


print(area())