#импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By


#класс будет иметь доступ ко всем атрибутам и методам класса-предка
class MainPage(BasePage):

    #метод нахождения элемента
    #browser хранится как аргумент класса BasePage
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
