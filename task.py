import os
from celery import Celery
from celeryconfig import CELERY_BROKER_BACKEND,result_backend
from flask import Flask, render_template, url_for, request, session
import json
import pika
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import cgi
import os
import sqlalchemy
import time
import re

celery = Celery('task',broker=CELERY_BROKER_BACKEND, backend=result_backend)


@celery.task(bind=True)
def salvar_ig():
    import os

    # from selenium.webdriver.common.keys import Keys
    # from selenium.webdriver.firefox.options import Options
    from selenium import webdriver

    #from selenium.webdriver.firefox.webdriver import FirefoxProfile
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument('window-size=1400,900')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--enable-sync')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-data-dir=C:\\Users\\joaon\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile

    # ------>Usar no deploy
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
    # Usar nos testes,
    #driver = webdriver.Chrome(executable_path=r"C:\\Users\\joaon\\Desktop\\selenium-webdriver\\chromedriver", chrome_options=chrome_options) #, chrome_options=chrome_options
    driver.get(url)
    import time
    SCROLL_PAUSE_TIME = 4
    # Get scroll height
    time.sleep(SCROLL_PAUSE_TIME)
    #--------------       INICIANDO => REPRODUZIR O Stories======
    btn = driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/div/div[3]/button")
    btn.click()
    time.sleep(1)
    ### ENCERRANDO REPRODUÇÂO DO Stories
    ##--------------       INICIANDO BUSCAR O SRC DO VIDEO
    src_cru_video = driver.find_element_by_xpath("//video[@class='y-yJ5  OFkrO ']")
    html_content = src_cru_video.get_attribute('innerHTML')
    a = html_content.split('src=')
    b = a[1]
    a = html_content.split('src=')
    c = b.replace('&amp;', '&')
    src_final = c.replace('"', "")
    src_final2 = src_final.replace(">", "")
    print("Link: ", src_final2)
    ## ENCERANDO BUSCA PELO LINK ===> ENCONTRADO
    ## --------------       COMEÇANDO FORMA DE SALVAR O VIDEO
    import urllib.request

    home = os.path.expanduser("..\\")
    download_path = os.path.join(home, "Video_IG.mp4")


    urllib.request.urlretrieve(src_final2, download_path)
    ##ENCERRANDO FORMA DE SALVAR O VIDEO
    ## --------------       Iniciando a análise do vídeo

    #driver.get(src_final2)
    driver.quit()
