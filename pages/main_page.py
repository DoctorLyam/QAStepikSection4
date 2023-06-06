#импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By
#испорт класса с селекторами
from .locators import MainPageLocators


#класс будет иметь доступ ко всем атрибутам и методам класса-предка
class MainPage(BasePage):

    #метод нахождения элемента
    #browser хранится как аргумент класса BasePage
    def go_to_login_page(self):
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
        #вместо строчки выше пишу:
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    #метод проверки наличия ссылки
    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        #вместо функции выше используем метод из BasePage, в котором мы прописали обработку исключения
        #теперь при возникновении исключения asset поймает False, иначе - True
        
        # assert self.is_element_present(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"
        
        #вместо строчки выше пишу (* указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"