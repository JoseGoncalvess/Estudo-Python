##Instalação do Selenium mais o WEbdriver(new-version)##
from selenium import webdriver #import webdriver
from webdriver_manager.chrome import ChromeDriverManager #importwebdrive-maneger
from selenium.webdriver.chrome.service import Service #import service do selenium
from selenium.webdriver.common.by import By

#Estrutura Montada
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.google.com")

