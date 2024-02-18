import random
import locale
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Set the locale to Spanish
locale.setlocale(locale.LC_TIME, 'es_CO.UTF-8')

opts = Options()
# opts.add_argument("--incognito")
opts.add_argument("--lang=es-CO")
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36")
service = Service(executable_path=r'./chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=opts)
driver.get("https://www.google.com/intl/es-419/gmail/about/")
driver.maximize_window()

timeImplyWait = 5
timeSleep = 5
day = random.randint(1, 30)
year = random.randint(1985, 2006)

WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located((By.LINK_TEXT, "Acceder"))).click()

WebDriverWait(driver, timeImplyWait).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'identifierId')]"))).send_keys(
    "qapruebascristhian@gmail.com")

WebDriverWait(driver, timeImplyWait).until(
    EC.presence_of_element_located((By.XPATH, "//span[@jsname='V67aGc'][contains(.,'Siguiente')]"))).click()
time.sleep(timeSleep)
