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
url = "https://www.researchgate.net/search/publication?q=%28smart+city%29+OR+%28cidade+inteligente%29+OR+%28ciudad+inteligente%29"

driver.get(url)

# 
result = driver.find_elements(By.XPATH, '//*[@id="rgw5_62a937b01dd9e"]/div/div[2]/div[2]/div/div[2]')