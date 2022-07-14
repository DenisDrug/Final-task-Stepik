from selenium.webdriver.common.by import By
import time
from pages.main_page import MainPage
from pages.basket_page import BasketPage



def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = "https://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(driver, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    time.sleep(2)
    page.go_to_basket()
    time.sleep(2)
    # page.check_basket_not_items()
    page.check_basket_empty()

