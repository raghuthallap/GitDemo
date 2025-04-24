import json

from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.signin_button = (By.ID, "signInBtn")



    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page

