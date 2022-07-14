from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class PageObject(BasePage):
    def go_to_add_item(self):
        add_item = self.driver.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
        add_item.click()

    def check_add_item_in_basket(self):
        item_basket = self.driver.find_element(By.XPATH, "//*[@id='messages']/div[1]/div/strong")
        item_basket_text = item_basket.text
        resalt = self.driver.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
        resalt_text = resalt.text
        assert item_basket_text == resalt_text, "Item not in basket"
        print(item_basket_text)

    def check_price_basket(self):
        item_price = self.driver.find_element(By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
        item_price_text = item_price.text
        resalt = self.driver.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
        rasalt_price = resalt.text
        assert item_price_text == rasalt_price, "Price not correct"
        print(item_price_text)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(By.XPATH, "//*[@id='messages']/div[1]/div/strong"), \
            "Success message is presented, but should not be"

    def should_be_login_link(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login_link")

    def email_user(self):
        email = str(time.time()) + "@fakemail.org"
        login = self.driver.find_element(By.CSS_SELECTOR, "#id_registration-email")
        login.send_keys(email)

    def password_user(self):
        password = str(time.time())
        enter_password = self.driver.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        enter_password.send_keys(password)
        # confirm = str(enter_password.send_keys(password))
        enter_password_confirm = self.driver.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        enter_password_confirm.send_keys(password)

    def register_new_user(self):
        user = self.driver.find_element(By.CSS_SELECTOR, "#register_form > button")
        user.click()

    def check_registration(self):
        account = self.driver.find_element(By.XPATH, "//a[@href = '/en-gb/accounts/']")
        account_text = account.text
        assert account_text == 'Account', "Кнопка регистрации не сработала"
