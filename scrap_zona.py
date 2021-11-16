from typing import Type
from pandas.core.frame import DataFrame
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import gspread
import pandas as pd

options = webdriver.ChromeOptions() # Usamos chrome, se podria usar otro.
#options.add_argument('--headless') # Chromium sin interfaz grafica
options.add_argument('--no-sandbox') # Seguridad
options.add_argument('--disable-dev-shm-usage') # configuracion de linux
#options.add_argument('--user-agent=""Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36""') # user agent

driver_path = '/home/belutrac/Documentos/scraping_deptos/chromedriver'
driver = webdriver.Chrome(driver_path,chrome_options = options)

next_page = 'https://www.zonaprop.com.ar/departamentos-alquiler-general-paz-cordoba-mas-de-2-habitaciones-orden-publicado-descendente.html'
driver.get(next_page)
WebDriverWait(driver, timeout=10)

driver.save_screenshot('screenshot_google.png')
datos = driver.find_elements_by_class_name('postingCardTitle')
a_tag = [a.find_element_by_tag_name("a").get_attribute("href") for a in datos]

print(a_tag)