from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

cookie_id = "bigCookie"
cookies_id = "cookies"
cookie_count = 0


service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")


WebDriverWait(driver, 5).until(
    ec.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, cookie_id)))

cookie = driver.find_element(By.ID, cookie_id)

while cookie_count < 100:
    cookie.click()
    cookie_count = int(driver.find_element(By.ID, cookies_id).text.split(" ")[0])

driver.quit()
