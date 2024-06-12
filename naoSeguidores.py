__author__ = "Guilherme Alves"
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

SLEEP_TIME = 4

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--no-proxy-server")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.instagram.com')
sleep(SLEEP_TIME)
username = driver.find_element(By.NAME, 'username')
username.send_keys('bandagigabyte') # APROVEITA E SEGUE MINHA BANDA!
password = driver.find_element(By.NAME, 'password')
password.send_keys('gigab@1995*')
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
sleep(SLEEP_TIME)

# with open(r'caminho\do\arquivo', 'r') as arquivo:
with open(r'C:\Users\ghfa_\OneDrive\Documentos\DEV\GIT\naoSeguidores\naoSeguidores.json', 'r') as arquivo:
    dados = json.load(arquivo)

    i=1
    for dado in dados:

        driver.get(dado)
        sleep(SLEEP_TIME)

        # FOLLOWING
        driver.find_element(By.XPATH, "//button/div/div").click()
        sleep(SLEEP_TIME)

        # UNFOLLOW
        driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]').click()
        sleep(SLEEP_TIME)
        print(f"UNFOLLOW: {dado} {[i]}")
        i+=1
