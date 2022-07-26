from datetime import date

print('=====.....ALISTAMENTO EB.....=====')
print()
atual = date.today().year
sexo = str(input('CANDIDATO(A), VOCÊ É HOMEM OU MULHER ?'))
if sexo == 'MULHER':
    print('MULHERES, SÓ MEDIANTE CONCURSO, ESTÁ DISPENSADA DO ALISTAMENTO, OK!')
    print('PRECISAMOS D EVOC~ES, VENHA FAZER PARTE DAS FORÇAS ARMADAS')
else:
    atual = date.today().year

    nasc = int(input(' EM QUÉ ANO VOCÊ NASCEU, GUERREIRO ?'))
    idade = atual - nasc

    print('QUEM NASCEU EM {}, TEM {} ANO(S) EM {}'.format(nasc, idade, atual))
    if idade == 18:
        print('GUERREIRO CHEGOU SUA HORA DE SERVIR, BRASIL!')
    elif idade <= 18:
        saldo = 18 - idade
        print('SEU ALISTAMENTO É SO DAQUI HÁ {} anos, ENTENDIDO!'.format(saldo))
    elif idade >= 18:
        saldo = idade - 18
    print('VOCÊ DEVERIA TER SE ALISTADO HÁ {}, ARREGO GUERREIRO!'.format(saldo))