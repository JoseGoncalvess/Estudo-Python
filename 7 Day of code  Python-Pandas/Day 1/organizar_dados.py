import pandas as pd
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
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
# Dia 3
# importação dea alguns
# Verificando a relação entre empréstimo e empréstimo de exemplar
emprestimos_completos['id_emprestimo'].value_counts()
# Note que o "id_emprestimo" é cada empréstimo realizado que pode ter 1 ou mais exemplares.

# Portando cada linha é o empréstimo de cada exemplar.
emprestimos_completos.loc[emprestimos_completos['id_emprestimo'] == 2560028]

# Quantos empréstimos foram realizados ao total?
# pego o tamanho e retiro as duplicatas
emprestimos_completos.count[emprestimos_completos['id_emprestimo'].drop_duplicates()]

# quantidades de exemplares emprestados
exemplares = len(emprestimos_completos)

# uma Analise masi porfdunda no caso por ano
emprestimos_data = pd.DataFrame(
    emprestimos_completos['data_emprestimo'].value_counts().reset_index())
# separo em duas colunas
emprestimos_data.columns = ['data', 'quantidade']
emprestimos_data['data'] = pd.to_datetime(emprestimos_data['data'])

# dividio podemos agroa agrupar por ano
# separo por ano e depois somo em cada ano
emprestimos_por_ano = emprestimos_data.groupby(
    by=emprestimos_data.data.dt.year).sum()
emprestimos_por_ano.index.name = 'ano'


# Configurando tema dos gráficos
# talver não funcione no python pc so do googlecolab
# o proprio exmeplo ja atende a nossa necessidade
sns.set_theme(context='notebook',
              style='darkgrid',
              palette='deep',
              font_scale=1.3,
              rc={"figure.figsize": (15, 8)}

              )
# definindo entrada d edados do grafico
ax = sns.lineplot(data=emprestimos_por_ano, x='ano', y='quantidade')
# definindpo texto para x e y
ax.set(xlabel=None, ylabel=None)
ax.tick_params(axis='x', rotation=30)
# editando quantidade int subistituindo a virgula por ponto
ax.yaxis.set_major_formatter(ticker.FuncFormatter(
    lambda x, p: format(int(x), ',').replace(',', '.')))
# titulo do grafico
ax.set_title('Quantidade de exemplares emprestados do SISBI por ano' +
             '\n', size=20, loc='left', weight='bold')

ax = ax


# mesmo esquema de dividir por ano
emprestimos_por_mes = emprestimos_data.groupby(
    by=emprestimos_data.data.dt.month).sum()
emprestimos_por_mes.index.name = 'mes'
# dicionario para ultilizar oname mes
dicionario_meses = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr',
                    5: 'Mai', 6: 'Jun', 7: 'Jul', 8: 'Ago',
                    9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}
# adicono o nome do index atravez do dicionario
emprestimos_por_mes.index = emprestimos_por_mes.index.map(dicionario_meses)

# gRAFICO DE MES

# definindo entrada de dados do grafico
ax = sns.lineplot(data=emprestimos_por_ano, x='mes', y='quantidade')
# definindpo texto para x e y
ax.set(xlabel=None, ylabel=None)
ax.tick_params(axis='x', rotation=30)
# editando quantidade int subistituindo a virgula por ponto
ax.yaxis.set_major_formatter(ticker.FuncFormatter(
    lambda x, p: format(int(x), ',').replace(',', '.')))
# titulo do grafico
ax.set_title('Quantidade de exemplares emprestados do SISBI por mês' +
             '\n', size=20, loc='left', weight='bold')

ax = ax
# ANALISE DO GRAFICO
# Pode-se visualizar que os meses com maiores números de exemplares emprestados foram em março e agosto.

# Por ser uma biblioteca universitária meses de férias como janeiro, julho e dezembro são os menores números.

# O que não é nada de novo, entretanto caso todos os colaboradores saírem de férias durante esse período não conseguiríamos manter todo o funcionamento da biblioteca.

# Principalmente com atividades de inventário que podem ocorrer anualmente ou de dois em dois anos e o melhor período seria de dezembro a janeiro.

# Então meses como maio, junho, outubro e novembro podem ser uma opção a ser considerada pela direção da biblioteca.

# Nota-se também a grande queda no mês de junho. Cabe aqui um alerta para se investigar mais, o que está ocorrendo e desenvolver estratégias e ações de marketing da biblioteca para que se aumente o número de exemplares emprestados.

# Como por exemplo: uma ação para que sejam realizados empréstimos de livros para a leitura nas férias de julho.


# Quantidade por mês
emprestimos_por_hora = emprestimos_data.groupby(
    by=emprestimos_data.data.dt.hour).sum()
emprestimos_por_hora.index.name = 'hora'
emprestimos_por_hora = emprestimos_por_hora.reset_index()
emprestimos_por_hora = emprestimos_por_hora.sort_values(
    ascending=True, by='quantidade')

# GERAR O GRAFICO DE HORAS
ax = sns.barplot(data=emprestimos_por_hora, y='quantidade', x='horas',
                 palette='Blues', hue='quantidade', dodge=False)  # Ordenar pela quantidade de exemplares emprestados
plt.legend([], [], frameon=False)  # Excluir a legenda do gráfico

ax.set(xlabel='Horário', ylabel=None)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(
    lambda x, p: format(int(x), ',').replace(',', '.')))
ax.set_title("Quantidade de exemplares emprestados do SISBI por faixa horária" +
             "\n", size=20, loc='left', weight='bold')
ax.text(s='Período de 2010 a 2020', x=-0.5, y=225000,
        fontsize=18, ha='left', color='gray')
ax = ax
