print("====DESAFIO0046====")
nome = str(input('olá, como você se chama ?'))
print('ola,{} bem vido ao HOUSE FINANCE, gostaria de financiar sua casa né !'.format(nome))


print('SO PRECISA RESPONDER UM PEQUENO QUESTIORNÁRIO! ')
casa = float(input("QUAL O VALOR DA CASA QUE VOÇÊ TEM EM MENTE ?"))
salário = float(input('QUAL A SUA RENDA SALÁRIAL ATUALMENTE?'))
ano = int(input('EM QUANTO TEMPO PRETENDE PAGAR?'))
parcela = casa / (ano * 12)
minimo = salário * 30 / 100
print()
print()
print('....Dados em Analise....')
print()
print()
print('Para FINANCEAR a casa de R${:.2f} em {} anos' .format(casa, ano),  end='')
print('As parcelas serão de R${:.2f}'.format(parcela))
if  parcela <= minimo:
    print('VEJA SÓ! PARABÉNS SEU  FINANCEAMENTO FOI APORVADO!')
    print(input('PODEMOS DA ENTRADA NA PAPELADA?'))
else:
    print('INFELISMENTE SEU FINANCEAMNETO FOI NEGADO')
    print('PODE TENTAR NOVAMENTE EM ALGUNS MESES!')
    print(input('JA OUVIU FALAR EM INVESTIMENTO ?'))