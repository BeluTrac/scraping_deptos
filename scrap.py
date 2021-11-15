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
from requests import post
from settings import BOT_TOKEN

def send_msg(msg, chat_id, bot_token):
    resp = post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage?"
        f"chat_id={chat_id}&parse_mode=Markdown&text={msg}"
    )
    return resp.json()

options = webdriver.ChromeOptions() # Usamos chrome, se podria usar otro.
options.add_argument('--headless') # Chromium sin interfaz grafica
options.add_argument('--no-sandbox') # Seguridad
options.add_argument('--disable-dev-shm-usage') # configuracion de linux
options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""') # user agent

driver_path = '/home/belutrac/Documentos/scraping_deptos/chromedriver'

driver = webdriver.Chrome(driver_path,chrome_options = options)

next_page = 'https://clasificados.lavoz.com.ar/inmuebles/departamentos/2-dormitorios?cantidad-de-dormitorios[0]=2-dormitorios&barrio=general-paz&operacion=alquileres'
links = []
while(1):
  # # Espero a que cargue la pagina
  driver.get(next_page)
  WebDriverWait(driver, timeout=1)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
  WebDriverWait(driver, timeout=1)

  algo = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]')
  algo2 = algo.find_elements_by_tag_name("a")

  for a in algo2:
    link = a.get_attribute("href")
    if (not link in links) and (link.startswith("https://clasificados.lavoz.com.ar/avisos/departamentos/")):
      links.append(link)
  siguiente_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/div[4]/nav/div/a')

  next_page = siguiente_button.get_attribute("href")

  if next_page == None:
    break



gs = gspread.service_account(filename = "/home/belutrac/Documentos/scraping_deptos/zeta-rush-332114-45d522cbfb7c.json")
hoja = gs.open_by_url("https://docs.google.com/spreadsheets/d/19HUgkqo3uPXozf7PeaGg1MIGnD0GPQOmZyKjMNnjCWc/edit#gid=0")
hoja1 = hoja.get_worksheet(0)
hoja_df = list(pd.DataFrame(hoja1.get_all_values())[0])

for i in links:
  if not i in hoja_df:
    send_msg(i,"2033255334",BOT_TOKEN)
    hoja_df.append(i)

hoja1.update([[i] for i in hoja_df])





