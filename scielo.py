from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


driverPath = Service(ChromeDriverManager().install())

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2, "profile.managed_default_content_settings.stylesheets": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=driverPath, options=chrome_options)
url = "https://search.scielo.org/?q=%28smart+city%29+OR+%28cidade+inteligente%29+OR+%28ciudad+inteligente%29&lang=pt&count=30&from=0&output=site&sort=&format=summary&fb=&page=1&filter%5Bin%5D%5B%5D=scl"

driver.get(url)

result = driver.find_element(By.CLASS_NAME, "results")
artigos = result.find_elements(By.CLASS_NAME, "item")




dados = []
for artigo in artigos:
    a = artigo.text.split("\n")
    arti = {
        "nome" : a[0],
        "autores" : a[2],
        "area_do_conhecimento" : a[3],
        "dado" : a[4],
        "ano" : a[4].split(","),
        "resume" : a[5],
        "link_do_artigo" : a[6] if len(a) == 7 else None 
    }
    dados.append(arti)



# Salvar
df = pd.DataFrame(columns=["nome", "autores", "area_do_conhecimento", "dado", "ano", "resume", "link_do_artigo"])
df = pd.concat([df, pd.DataFrame.from_records([prod for prod in dados])], ignore_index=True)
df.to_csv("dados.csv", index = False)

