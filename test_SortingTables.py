import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    browserSortedList = []
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    driver.maximize_window()

    # expectedSortedItemsList = ['Almond','Apple','Banana','Beans','Brinjal']

    driver.find_element(By.CSS_SELECTOR, "table thead tr th:nth-child(1)").click()
    itemsList = driver.find_elements(By.CSS_SELECTOR, "table tbody tr td:nth-child(1)")

    for item in itemsList:
        browserSortedList.append(item.text)

    print(browserSortedList)

    SortedItemsList = browserSortedList.copy()
    browserSortedList.sort()

    assert browserSortedList == SortedItemsList

    time.sleep(5)


