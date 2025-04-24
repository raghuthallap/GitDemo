# pytest -m smoke //Tagging
# pytest -m 10//pytest -xdist plugin to run in parallel

# pytest -n 2 -m smoke --browser_name firefox --html=reports/report.html



import json
import pytest


from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage

test_data_path = "data/test_e2eTestFramework.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    driver.maximize_window()
    loginpage = LoginPage(driver)
    print(loginpage.getTitle())
    shop_page = loginpage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    shop_page.addProductToCart(test_list_item["productName"])
    print(shop_page.getTitle())
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enterDeliveryAddress("ind")
    checkout_confirmation.validateOrder()
    print(checkout_confirmation.getTitle())

#orig code without page obj imp


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
