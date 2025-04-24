from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import Checkout_Confirmation
from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.CSS_SELECTOR, "div[class='card h-100']")
        self.checkout_button = (By.XPATH, "//a[contains(text(),'Checkout')]")



    def addProductToCart(self,product_name):
        # a[href*="shop"] #//a[contains(@href,"shop")]
        self.driver.find_element(*self.shop_link).click()

        products = self.driver.find_elements(*self.product_cards)
        for product in products:
            if product.find_element(By.TAG_NAME, "h4").text == product_name:
                product.find_element(By.CSS_SELECTOR, "div button").click()

    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation



