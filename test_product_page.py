import time
import pytest
from pages.product_page import PageObject
from pages.basket_page import BasketPage

#2
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(driver, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    time.sleep(2)
    page.go_to_add_item()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.check_add_item_in_basket()
    time.sleep(2)
    page.check_price_basket()

#3
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    page = BasketPage(driver, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    time.sleep(2)
    page.go_to_basket()
    time.sleep(2)
    page.check_basket_empty()

#4
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(driver, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)
    page.check_register_form()
    page.check_login_form()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = PageObject(driver, link)
        page.open()
        page.email_user()
        time.sleep(2)
        page.password_user()
        time.sleep(2)
        page.register_new_user()
        time.sleep(2)
        page.check_registration()

# 1
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = PageObject(driver,
                          link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        time.sleep(2)
        page.go_to_add_item()
        time.sleep(2)
        page.solve_quiz_and_get_code()
        time.sleep(2)
        page.check_add_item_in_basket()
        time.sleep(2)
        page.check_price_basket()

    @pytest.mark.xfail
    def test_user_cant_see_success_message(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = PageObject(driver,
                          link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.is_not_element_present()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(driver, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_add_item()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    page.is_not_element_present()

@pytest.mark.xfail
def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(driver, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.is_not_element_present()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(driver, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_add_item()
    page.is_disappeared()

@pytest.mark.xfail
def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(driver, link)
    page.open()
    page.should_be_login_link()










