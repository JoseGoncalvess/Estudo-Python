from lib2to3.pgen2 import driver
from webbrowser import Chrome
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

contato['+5587991650328']
text = '''Olá, boa tarde! Este é o *Whatsapp Oficial da DCA- Distribuidora de Cimentos Arcoverde!*

Fomos sinalizados que você recebeu seu pedido, assim estamos lançando uma pesquisa rápida para podermos melhorar cada vez mais nossos serviços!

Basta clicar no link abaixo e responder algumas perguntas, não leva nem 1 minuto:
*Pesquisa de satisfação:*

 https://bit.ly/Dca-Pesquisa-de-satisfação

*DCA - Distribuidora de Cimento Arcoverde.🚚*'''

driver = webdriver, Chrome(ChromeDriverManager().install())
driver.get(f'https://web.whatsapp.com/send?={contato[0]}&text={texto}')
