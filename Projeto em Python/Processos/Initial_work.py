import pyautogui
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
# #SETAR MEU NAVEGADOR
driver = webdriver.Chrome(ChromeDriverManager().install())
# ABRO A GUI PRINCIPAL
driver.get('https://web.whatsapp.com/')
sleep(2)
# ABRO UM NOVA GUI (FACEBOOK)
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://business.facebook.com/')
pyautogui.press('enter')
sleep(3)
# ABRO UM NOVA GUI (CANVAS)
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://www.canva.com/')
pyautogui.press('enter')
sleep(2)
