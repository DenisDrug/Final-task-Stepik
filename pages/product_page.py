from selenium.webdriver.common.by import By
from .base_page import BasePage

class PageObject(BasePage):
    def go_to_add_item(self):
        add_item = self.driver.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
        add_item.click()

    def check_add_item_in_basket(self):
        item_basket = self.driver.find_element(By.XPATH, "//*[@id='messages']/div[1]/div/strong")
        item_basket_text = item_basket.text
        assert item_basket_text == self.driver.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1"), "Item not in basket"
        print(item_basket_text)
    def check_price_basket(self):
        item_price = self.driver.find_element(By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
        item_price_text = item_price.text
        assert item_price_text == self.driver.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]"), "Price not correct"
        print(item_price_text)


