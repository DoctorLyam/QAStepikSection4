#файл реализации методов проверки страницы с логином
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    #вызов всех трех методов проверки ниже
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #driver.current_url достает URL текущей страницы
        login_url = self.browser.current_url
        assert "login" in login_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL)
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(LoginPageLocators.REG_EMAIL)
        assert self.is_element_present(LoginPageLocators.REG_PASS)
        assert self.is_element_present(LoginPageLocators.REG_PASS2)