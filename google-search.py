import os   #Importa biblioteca de sistema operacional para setar uma variável de ambiente com o caminho do webdriver (chromedrive)
import time #Importa biblioteca respinsáve por criar Delay e Manipular operações de tempo

#Importa bibliotecas necessárias do Selenium para simular interação humana entre as páginas.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


#Método que carrega o browser, configura e retorna o objeto de 'driver' referente a interação no browser.
def LoadBrowser():
    executable_path = "/home/rayan/Documents/scientific_python/chromedrive"
    os.environ["webdriver.chrome.driver"] = executable_path

    chrome_options = Options()
    

    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
    driver.get("https://google.com")
    time.sleep(1)
    return driver    



#Método que faz a busca no google e obtem a quantidade de resultados através da varredura na estrutura DOM da página HTML de resultado
#Pelo driver.
def GoogleSearch(driver):
	
	search_field = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
	search_field.send_keys('Cristiano Ronaldo Aveiro dos Santos')
	
	search_field.send_keys(Keys.ENTER)
	
	time.sleep(1)
	
	results_google = driver.find_element_by_id('result-stats').text
	print(results_google)



#Executa os métodos.
driver = LoadBrowser()
GoogleSearch(driver)

	
	
