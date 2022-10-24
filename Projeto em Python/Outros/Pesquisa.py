from selenium import webdriver
##baixando o google chome do site##
navegador = webdriver.Chrome()
navegador.get('https://www.google.com/chrome/?brand=BNSD&gclid=Cj0KCQjwof6WBhD4ARIsAOi65ahH-5DVbw-hojRN-3IR7SWD_UVnT3W_iVpPlljLWUCeYCeRdXHQB3gaAujMEALw_wcB&gclsrc=aw.ds')
navegador.find_element_by_xpath('//*[@id="js-download-hero"]').click()