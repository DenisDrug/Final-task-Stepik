from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"