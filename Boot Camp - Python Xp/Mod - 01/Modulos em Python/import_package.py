import colorama #PAKAGER D ECOLOR DO TEXTO
#TEXTO NORMAL
print('TOU NORMAL')
#TEXTO COM A  COR AZUL
print(colorama.Fore.BLUE+'Mudei')
#TEXTO COM O FUNDO AZUL E COR BRANCA
print(colorama.Back.BLUE+ colorama.Fore.WHITE +'Mudei')
#RESET DO ESTILOS
print(colorama.Style.RESET_ALL+'Mudei')
