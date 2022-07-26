import time
new= int(input('COMEÇO DA SEQEUNCIA:'))
end = int(input('FIM DA SEQUENCIA:'))
var = str(input('PAR OU IMPAR?'))
if var == 'par':
   n = 2
else:
    n = 3
for c in range(new,end, n):
    print(c)
