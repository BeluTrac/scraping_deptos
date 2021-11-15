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
options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""') # user agent

driver_path = '/home/belutrac/Documentos/scraping_deptos/chromedriver'
driver = webdriver.Chrome(driver_path,chrome_options = options)

next_page = 'https://inmuebles.mercadolibre.com.ar/departamentos/alquiler/2-dormitorios/cordoba/cordoba/general-paz/_NoIndex_True#applied_filter_id%3Dneighborhood%26applied_filter_name%3DBarrios%26applied_filter_order%3D2%26applied_value_id%3DTUxBQkdFTjc0OTVa%26applied_value_name%3DGeneral+Paz%26applied_value_order%3D19%26applied_value_results%3D24%26is_custom%3Dfalse'
driver.get(next_page)
WebDriverWait(driver, timeout=10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
WebDriverWait(driver, timeout=10)

meli_links = []
algo = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/section').find_elements_by_tag_name("ol")

for i in algo:
    algo2 = i.find_elements_by_class_name("ui-search-layout__item")
    for i in algo2:
        meli_links.append(i.find_element_by_tag_name("a").get_attribute("href"))

print(meli_links)
driver.close()