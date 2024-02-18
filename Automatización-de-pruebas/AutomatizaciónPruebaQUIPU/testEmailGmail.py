import random
import locale
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
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
driver.get("https://accounts.google.com/signup")
driver.maximize_window()

timeImplyWait = 5
timeSleep = 5
day = random.randint(1, 30)
year = random.randint(1985, 2006)
cellPhone = 3212861012

(WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))
 .send_keys("QA Cristhian"))
(WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']")))
 .send_keys("Montaño"))

WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located((By.XPATH, "//*[@id='collectNameNext']/div"
                                                                                     "/button"))).click()
time.sleep(timeSleep)
WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located((By.ID, "day"))).send_keys(day)
mes_dropdown = WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located((By.ID, "month")))
mes_dropdown.send_keys("Febrero")
genero_dropdown = WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located((By.ID, "gender")))
genero_dropdown.send_keys("Femenino")
WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located((By.ID, "year"))).send_keys(year)
WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located((By.XPATH, "//*[@id='birthdaygenderNext']/div"
                                                                                     "/button"))).click()

try:
    email_dropdown = WebDriverWait(driver, timeImplyWait).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'identifierId')]")))
    print(email_dropdown)
    print("Sección A")
    try:
        email_dropdown.send_keys("qapruebatecnica@gamil.com")
        print("SE genero correos")

        WebDriverWait(driver, timeImplyWait).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='next']/div/button"))).click()

    except TimeoutException as ex:
        print("No se genero correos")
except TimeoutException as ex:
    email_dropdown = WebDriverWait(driver, timeImplyWait).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='sSzDje zVkt0c'][contains(.,'Crear tu propia dirección de Gmail')]")))
    email_dropdown.click()
    print("Sección B")
    try:
        WebDriverWait(driver, timeImplyWait).until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'zHQkBf', ' ' ))]"))).send_keys(
            "qapruebatecnica")
        print("Se genero correos")
        WebDriverWait(driver, timeImplyWait).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='next']/div/button"))).click()

    except TimeoutException as ex:
        print("No se genero correos")

WebDriverWait(driver, timeImplyWait).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input'))).send_keys("qaprueba123")

WebDriverWait(driver, timeImplyWait).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'))).send_keys(
    "qaprueba123")

WebDriverWait(driver, timeImplyWait).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="createpasswordNext"]/div/button'))).click()

WebDriverWait(driver, timeImplyWait).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'phoneNumberId')]"))).send_keys(cellPhone)

WebDriverWait(driver, timeImplyWait).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Siguiente')]"))).click()

time.sleep(timeSleep)
