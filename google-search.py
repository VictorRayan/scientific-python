import pandas as pd

import os   #Importa biblioteca de sistema operacional para setar uma variável de ambiente com o caminho do webdriver (chromedrive)

#Importa bibliotecas necessárias do Selenium para simular interação humana entre as páginas.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import json #Importa biblioteca para manipular estrutura de dados Json



# Show all columns in pandas dataframe when printing to stdout
pd.set_option("display.max_columns", None)

datafile='/home/rayan/Documents/scientific_python/magnetic-dimensionality-v100.csv'
df0 = pd.read_csv(datafile, ';')

#print(df0.keys())

# Drop all the columns except these ones
df = df0[['icsd_code','dimension', 'chemical_structural_formula', 'num_atoms', 'space_group_symmetry', 'number_index', 'structure_type', 'valence', 'metal_neigh_coordination', 'partial_occupancy']].copy()

# selected only materials with a given number of atoms, two-dimensional and no partial occupancy of atomic sites
df_y = (df[ (df.num_atoms<=3) & (df.dimension==2) & (df.partial_occupancy=='no') ])

#Lista com todos os termos do DataFrame que atenderam a condiçaõ estabelecida
lista_de_materiais = list(df_y['chemical_structural_formula'])


#Remove spaces
lista_de_materiais=[ ''.join(m.split(' ')) for m in lista_de_materiais ] # Remove spaces

print(lista_de_materiais)

# List of words to be searched for
lista_de_termos=['magnetic','metal','insulator']



# Dictionary with the data gathered in the search
gathered_data={'material':[],'search_word':[],'search_result':[]}

#Método que carrega o browser, configura e retorna o objeto de 'driver' referente a interação no browser.
def LoadBrowser():
    executable_path = "./chromedrive"
    os.environ["webdriver.chrome.driver"] = executable_path

    chrome_options = Options()
    

    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
    driver.get("https://google.com")
    return driver    



#Método que faz a busca no google e obtem a quantidade de resultados através da varredura na estrutura DOM da página HTML de resultado
#Pelo driver.


#REALIZA A BUSCA DOS TERMOS PASSADOS COMO PARAMETRO
#parametro "driver" - inicaliza o navegador
#parametro "term" - envia ao metodos os termos que serão pesquisados            
def GoogleSearch(driver, term):
	driver.get("https://google.com")

	search_field = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
	search_field.send_keys(term)
	search_field.send_keys(Keys.ENTER)
	results_google = driver.find_element_by_id('result-stats').text
	return (term+" "+results_google)


#BUSCA DOS DADOS DO DATAFRAME DE MATERIAIS E TERMOS NO GOOGLE
driver = LoadBrowser()

try:
  for mat in lista_de_materiais:
    for word in lista_de_termos:
      gathered_data['material'].append(mat)
      gathered_data['search_word'].append(word)
      gathered_data['search_result'].append(GoogleSearch(driver, mat+" "+word))
except: 
    print('hello world')


'''
file_json = open('gathered_data.json', 'w')
file_json.write(json.dumps(gathered_data))
file_json.close()
gathered_df = pd.read_json('gathered_data.json')
gathered_df.to_csv('gathered_data.csv')
'''
df_from_json = pd.DataFrame.from_dict(gathered_data, orient='index')
df_from_json = df.transpose()
df_from_json.to_csv('gathered_data.csv')
