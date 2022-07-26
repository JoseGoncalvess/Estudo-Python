#FRASE, SEM ESPAÇO, MAISUSCULA
frase = str(input('DIGITE UMA FRASE:')).strip().upper()
words = frase.split() #SEPARA EM PALAVRAS EM UMA LISTA
all_unids = ''.join(words)
invers= ''
for letra in range(len(all_unids) - 1, -1, -1):#COMEÇA DO FINAL DA PALAVRA E VAI VOLTADO UMA CASA
    invers += all_unids[letra]
print('O INVERSO DE {} É {}'.format(all_unids,invers))
if invers == all_unids:
    print('VEJA SÓ TEMPOS UMA PALINDROMO')
else:
    print('ESTÁ FRASE INFELISMENTE NÃO É UM PALINDROMO')