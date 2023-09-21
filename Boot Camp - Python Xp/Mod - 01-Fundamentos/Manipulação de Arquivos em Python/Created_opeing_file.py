# 'R' = Leitura padrão
# 'w' = Escrita, cria arquivo caso ele não exista ou subistitui o atual
# 'x' = Escrita, cria arquivo caso ele  exista retorna um erro
# 'a' = Escrita, cria arquivo caso ele  exista add infomações ao final dele
# 't' = Abri arquivo no mod texto padrão
# 'b' = Abri arquivo no mod binario
 
 #LEITURA DE ARQUIVO
aquivo= open('../Estudo-Python/Boot Camp - Python Xp/Mod - 01/Manipulação de Arquivos em Python/file/file_text.txt', 'r')
#FECHAMENTO DO ARQUIVO
aquivo.close()


#CRIA  O ARQUIVO E SOBRESCREVE SE JÁ EXISTIR
aquivo2= open('../Estudo-Python/Boot Camp - Python Xp/Mod - 01/Manipulação de Arquivos em Python/file/file_W.txt', 'w')
#FECHAMENTO DO ARQUIVO
aquivo.close()


#CRIA  O ARQUIVO E RETORNA ERRO SE JÁ EXISTIR
aquivo2= open('../Estudo-Python/Boot Camp - Python Xp/Mod - 01/Manipulação de Arquivos em Python/file/file_W2.txt', 'x')
#FECHAMENTO DO ARQUIVO
aquivo.close()

#ABRO OA RQUIVO PARA ESCREVER E EXPECIFICO O MODO QUE NO CASO É TEXTO
aquivo2= open('../Estudo-Python/Boot Camp - Python Xp/Mod - 01/Manipulação de Arquivos em Python/file/file_W.txt', 'at')
#FECHAMENTO DO ARQUIVO
aquivo.close()