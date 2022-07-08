from selenium.webdriver.common.by import By
import time
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


# url = "http://selenium1py.pythonanywhere.com/"
#
# def go_to_login_page(driver):
#     login_link = driver.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()
#
# def test_guest_can_go_to_login_page(driver):
#    driver.get(url)
#    go_to_login_page(driver)



