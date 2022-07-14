import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage

class BasketPage(BasePage):
    def check_basket_empty(self):
        basket = self.driver.find_element(By.CSS_SELECTOR, "#content_inner > p")
        basket_text = basket.text
        print(basket_text)
        assert basket_text == "Your basket is empty. Continue shopping"

    def check_basket_not_items(self):
        basket_available = self.driver.find_element(By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
        basket_available_text = basket_available.text
        print(basket_available_text)
        assert basket_available_text == "Items to buy now", "Basket are empty"

