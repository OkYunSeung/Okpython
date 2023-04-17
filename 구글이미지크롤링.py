import requests
import bs4
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tqdm.notebook import tqdm
import warnings
warnings.simplefilter('ignore')
import urllib.request 


driver = Chrome('./chromedriver')

query = "조코딩"

page_url = "https://www.google.co.kr/imghp?hl=ko"

driver.get(page_url)



driver.find_element(By.CLASS_NAME, 'gLFyf').send_keys(query + Keys.ENTER)
for _ in range(10):    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

driver.find_element(By.CLASS_NAME, 'mye4qd').click()

images = driver.find_elements(By.CLASS_NAME, 'rg_i.Q4LuWd')

count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element(By.CLASS_NAME, 'n3VNCb.pT0Scc.KAlRDb').get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count += 1
    except:
        pass
    

driver.close()