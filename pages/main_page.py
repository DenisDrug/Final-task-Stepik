from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.driver.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        # return LoginPage(driver=self.driver, link=self.driver.current_link)
        alert = self.driver.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login_link_invalid")