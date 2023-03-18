import pandas as pd
# IMPORTAR OS DADOS DA BIBLIOTECA
dados_20101 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20101.csv')

dados_20102 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20102.csv')
dados_20111 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20111.csv')
dados_20112 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20112.csv')
dados_20121 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20121.csv')
dados_20122 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20122.csv')
dados_20131 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20131.csv')
dados_20132 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20132.csv')
dados_20141 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20141.csv')
dados_20142 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20142.csv')
dados_20151 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20151.csv')
dados_20152 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20152.csv')
dados_20161 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20161.csv')
dados_20162 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20162.csv')
dados_20171 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20171.csv')
dados_20172 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20172.csv')
dados_20181 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20181.csv')
dados_20182 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20182.csv')
dados_20191 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20191.csv')
dados_20192 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20192.csv')
dados_20201 = pd.read_csv(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_emprestimos/emprestimos-20201.csv')
# CONCATENANDO OS DADOS
emprestimos_bibliotecas = pd.concat([dados_20101, dados_20102, dados_20111, dados_20112, dados_20121, dados_20122, dados_20131, dados_20132, dados_20141,
                                    dados_20142, dados_20151, dados_20152, dados_20161, dados_20162, dados_20171, dados_20172, dados_20181, dados_20182, dados_20191, dados_20192, dados_20201])

# VERIFICANDO DUPLICATAS

# EXCLUINDO DUPLICATAS
emprestimos_bibliotecas = emprestimos_bibliotecas.drop_duplicates()
# DEFINIDNO O NUMERO DE COLUNAS
emprestimos_bibliotecas.head()

# IMPORTANTANDO DADOS DOS EXEMPLARES
dados_exemplares = pd.read_parquet(
    'C:/Users/DCA/Documents/Estudo-Python/7 Day of code  Python-Pandas/Day 1/dados_exemplares.parquet')

# UNIFICANDO TODOS OS DADOS
# MESCLANO OS DADOS
emprestimos_completos = emprestimos_bibliotecas.merge(dados_exemplares)


# CRIANDO UMA NOVA COLUNA APARTIR A 2
CDU_list = []
for cdu in emprestimos_completos['localização']:
    if(cdu < 100):
        CDU_list.append('Ciência e Conhecimento')
    elif(cdu < 200):
        CDU_list.append('Filosofia e Psicologia')
    elif(cdu < 300):
        CDU_list.append('Religião')
    elif(cdu < 400):
        CDU_list.append('Ci~encias Sociais')
    elif(cdu < 500):
        CDU_list.append('Provisoriamente não Ocupada')
    elif(cdu < 600):
        CDU_list.append('Matemática e ciencias naturais')
    elif(cdu < 700):
        CDU_list.append('Ci~encia aplicada')
    elif(cdu < 800):
        CDU_list.append('Belas Artes')
    elif(cdu < 900):
        CDU_list.append('Linguagem, Lingua, Linguistica')
    else:
        CDU_list.append('GEografia, Biografia, História')

emprestimos_completos['CDU Geral'] = CDU_list
emprestimos_completos.head()


# excluir colunas que não faz sentindo
# ultilizo o emtodo drop para efetuar a exclussão apssadno oa coluna = posição
emprestimos_completos.drop(columns=['registro_sistema'], inplace=True)
#
emprestimos_completos['matricula_ou_siape'] = emprestimos_completos['matricula_ou_siape'].astype(
    'string')
