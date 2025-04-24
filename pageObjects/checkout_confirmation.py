from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserutils import BrowserUtils


#my code
# class Checkout_Confirmation:
#
#     def __init__(self,driver):
#         self.driver = driver
#         self.checkout_button = (By.XPATH, "//button[contains(text(),'Checkout')]")
#
#
#     def checkout(self):
#          self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()


#tutorial code
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
#
class Checkout_Confirmation(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enterDeliveryAddress(self, countryName):
        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validateOrder(self):
        successText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in successText

    def getTitle(self):
        return self.driver.title

#my orig code without page obj imp
 # driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
    #
    # driver.find_element(By.ID, "country").send_keys("ind")
    #
    # wait = WebDriverWait(driver, 5)
    # countries_locator = (By.CSS_SELECTOR, "div[class='suggestions'] li")
    # wait.until(expected_conditions.visibility_of_element_located(countries_locator))
    #
    # countries = driver.find_elements(*countries_locator)
    # for country in countries:
    #     if country.text == "India":
    #         country.click()
    #         break
    #
    # label_element = driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']")
    # label_element.find_element(By.TAG_NAME, "a").click()
    #
    # dialog_element = driver.find_element(By.XPATH, "//div[@class='nsm-dialog-animation-fade nsm-dialog nsm-dialog-open']")
    # dialog_element.find_element(By.XPATH, "button[text()='Close']").click()
    # label_element.find_element(By.TAG_NAME, "a").click()
    # dialog_element.find_element(By.XPATH, "//button/img").click()
    #
    # label_element.click()
    #
    # driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    #
    # wait = WebDriverWait(driver, 2)
    # div_locator = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    # wait.until(expected_conditions.visibility_of_element_located(div_locator))
    # div_element = driver.find_element(*div_locator)
    # alert_message = div_element.text
    # assert "Success! Thank you" in alert_message
    # div_element.find_element(By.TAG_NAME, "a").click()
    #
    # time.sleep(5)

