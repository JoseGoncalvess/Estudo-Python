# #ADD INFORMAÇÃO AO ARQUIVO 
# #ABRO OA RQUIVO E EM SEGUDA ESCREVO NELE
# aq= open('Boot Camp - Python Xp\Mod - 01/Manipulação de Arquivos em Python/file/city.txt','a')
# aq.write('SP; São Paulo; 1290000\n')
# aq.close()

#passo uma lsita comas indromações e vou escrevedo linha a linha 
lines=['\nBA; Macaubas; 190000\n','RS; Rio Grande do Sul; 120000\n','AM; Manaus; 1404500\n'
'RJ; Rio de Janeiro; 1945400\n']
aq= open('Boot Camp - Python Xp\Mod - 01/Manipulação de Arquivos em Python/file/city.txt','a')
aq.writelines(lines)
aq.close()
