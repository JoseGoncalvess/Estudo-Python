import pyautogui
import time

#ALERTA DO BOT
pyautogui.alert('BOM DIA Sr.GONÇALVES vAMOS oRGANIZAR A SUA ÁREA DE TRABALHO! ')


#INICIO DA ORGANIZAÇÃO
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press("enter")
time.sleep(3)

#ABRIR O WHATSAPP
pyautogui.write("https://web.whatsapp.com/")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")
time.sleep(2)

#ABRIR O FACEBOOKBUSNISES
pyautogui.write("https://business.facebook.com/")
pyautogui.press("enter")
time.sleep(2)

#ABRIR O CANVA
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://www.canva.com/")
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("winleft", "D")

pyautogui.alert('Sr.GONÇALVES TUDO CERTO! TENHA UM BOM DIA DE TRABALHO!')

