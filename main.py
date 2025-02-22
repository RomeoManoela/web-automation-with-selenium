from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

WebDriverWait(driver, 5).until(
    ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Tech With Tim" + Keys.ENTER)

WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

time.sleep(25)
driver.quit()
