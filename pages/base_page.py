import math
from telnetlib import EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage():
    def __init__(self, driver, link):
        self.driver = driver
        self.link = link

    def open(self):
        self.driver.get(self.link)

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.driver.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.driver.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def check_register_form(self):
        assert self.driver.find_element(By.CSS_SELECTOR, '#register_form'), "Form register is not presented"

    def check_login_form(self):
        assert self.driver.find_element(By.CSS_SELECTOR, '#login_form'), "Form login is not presented"

    def go_to_basket(self):
        basket = self.driver.find_element(By.XPATH, "//a[@class='btn btn-default']")
        basket.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"


