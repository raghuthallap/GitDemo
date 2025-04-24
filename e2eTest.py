import time
from xml.etree.ElementPath import findtext

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

#a[href*="shop"] #//a[contains(@href,"shop")]
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()

products = driver.find_elements(By.CSS_SELECTOR,"div[class='card h-100']")
for product in products:
    if product.find_element(By.TAG_NAME,"h4").text == "Blackberry":
        product.find_element(By.CSS_SELECTOR,"div button").click()

driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()

driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()

driver.find_element(By.ID,"country").send_keys("ind")

wait = WebDriverWait(driver,5)
countries_locator = (By.CSS_SELECTOR,"div[class='suggestions'] li")
wait.until(expected_conditions.visibility_of_element_located(countries_locator))

countries = driver.find_elements(*countries_locator)
for country in countries:
    if country.text == "India":
        country.click()
        break

label_element = driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']")
label_element.find_element(By.TAG_NAME, "a").click()

dialog_element = driver.find_element(By.XPATH,"//div[@class='nsm-dialog-animation-fade nsm-dialog nsm-dialog-open']")
dialog_element.find_element(By.XPATH,"button[text()='Close']").click()
label_element.find_element(By.TAG_NAME, "a").click()
dialog_element.find_element(By.XPATH,"//button/img").click()

label_element.click()

driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

wait = WebDriverWait(driver,2)
div_locator = (By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
wait.until(expected_conditions.visibility_of_element_located(div_locator))
div_element = driver.find_element(*div_locator)
alert_message = div_element.text
assert "Success! Thank you" in alert_message
div_element.find_element(By.TAG_NAME,"a").click()


time.sleep(5)