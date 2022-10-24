##############################################################################################################################
# ██████  ███████ ███████  ██████  ██    ██ ██ ███████  █████  ██
# ██   ██ ██      ██      ██    ██ ██    ██ ██ ██      ██   ██ ██
# ██████  █████   ███████ ██    ██ ██    ██ ██ ███████ ███████ ██
# ██      ██           ██ ██ ▄▄ ██ ██    ██ ██      ██ ██   ██
# ██      ███████ ███████  ██████   ██████  ██ ███████ ██   ██ ██
#                             ▀▀
####################################################################################################################################################
# Bibliotecas necesseraias para rodar (todas podem ser instaladas com pip install)
import pywhatkit
import keyboard
import time
from datetime import datetime
################################################################################################
# Para quem eu vou enviar
contatos = ['+5584996709857', '+558399822278', '+558396054738']
################################################################################################
# intervalo de envio
while len(contatos) >= 1:
    # Envio da Menssagem
    pywhatkit.sendwhatmsg(contatos[0], '''

        
        Olá, Boa tarde! Este é o *Whatsapp Oficial da DCA- Distribuidora de Cimentos Arcoverde!*

Fomos sinalizados que você recebeu seu pedido, assim estamos lançando uma pesquisa rápida para podermos melhorar cada vez mais nossos serviços!

Basta clicar no link abaixo e responder algumas perguntas, não leva nem 1 minuto:
Pesquisa de satisfação:

 https://bit.ly/Dca-Pesquisa-de-satisfação

*DCA - Distribuidora de Cimento Arcoverde.*

''', datetime.now().hour, datetime.now().minute + 1)
    # Durante o codgo ele não envia a menssagem para o memso contato
    del contatos[0]
    time.sleep(15)

    keyboard.press_and_release('ctrl + w')
