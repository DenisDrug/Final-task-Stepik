import math
import time
import pytest
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from pages.product_page import PageObject



# def test_guest_can_add_product_to_basket(driver):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = PageObject(driver, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     time.sleep(1)
#     button = PageObject(driver,link)
#     time.sleep(1)
#     button.go_to_add_item()
#     time.sleep(1)
#     alert = driver.switch_to.alert
#     x = alert.text.split(" ")[2]
#     answer = str(math.log(abs((12 * math.sin(float(x))))))
#     alert.send_keys(answer)
#     alert.accept()
#     try:
#         alert = driver.switch_to.alert
#         alert_text = alert.text
#         print(f"Your code: {alert_text}")
#         alert.accept()
#     except NoAlertPresentException:
#         print("No second alert presented")


@pytest.mark.parametrize('num', [*range(0,6), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(driver, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = PageObject(driver, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    time.sleep(1)
    button = PageObject(driver, link)
    time.sleep(1)
    button.go_to_add_item()
    time.sleep(1)
    alert = driver.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")


    item_basket = driver.find_element(By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    item_basket_text = item_basket.text
    resalt = driver.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    resalt_text = resalt.text
    assert item_basket_text == resalt_text, "Item not in basket"
    print(item_basket_text)

    item_price = driver.find_element(By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    item_price_text = item_price.text
    resalt = driver.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    rasalt_price = resalt.text
    assert item_price_text == rasalt_price, "Price not correct"
    print(item_price_text)

    # item = PageObject(driver, link)
    # item.check_add_item_in_basket
    # price = PageObject(driver, link)
    # price.check_price_basket







