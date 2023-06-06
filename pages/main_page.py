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

    #метод проверки наличия ссылки
    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        #вместо функции выше используем метод из BasePage, в котором мы прописали обработку исключения
        #теперь при вощникновении исключения asset поймает False, иначе - True
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"