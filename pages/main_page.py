#импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By
#испорт класса с селекторами
from .locators import MainPageLocators

#ПЕРЕХОД МЕЖДУ СТРАНИЦАМИ (СПОСОБ 1):
#from .login_page import LoginPage
#ПЛАН СПОСОБА 1:
#в методе клика после клика возвращаем страницу с логином через создание объекта класса LoginPage()
#в основном, тестовом, файле после метода открытия страницы - метод клика и возвращения страницы логина (go_to_login_page), 
# затем метод проверок (should_be_login_page)

#СПОСОБ 2 - инициализация страницы с логином в теле теста в глвном файле (test_main_page.py)

#класс будет иметь доступ ко всем атрибутам и методам класса-предка
class MainPage(BasePage):

    #метод нахождения элемента
    #browser хранится как аргумент класса BasePage
    def go_to_login_page(self):
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
        #вместо строчки выше пишу:
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        
        #ПЕРЕХОД МЕЖДУ СТРАНИЦАМИ (СПОСОБ 1):
        #после клика по кнопке со ссылкой переходим на страницу авторизации и регистрации
        #инициализация нового объекта (страницы с логином) и возврат его
        #LoginPage() имеет родителя BasePage()
        #return LoginPage(browser=self.browser, url=self.browser.current_url) 

        #после этого добавляем в тестовую функцию в файле (test_main_page):
        #login_page = page.go_to_login_page()
        #login_page.should_be_login_page()
        #, где присваиваем переменной объект с методом клика и перехода на другую страницу,
        # а потом вызываем метод из LoginPage(BasePage), который вызывает три метода с проверками полей

    #метод проверки наличия ссылки
    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        #вместо функции выше используем метод из BasePage, в котором мы прописали обработку исключения
        #теперь при возникновении исключения asset поймает False, иначе - True
        
        # assert self.is_element_present(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"
        
        #вместо строчки выше пишу (* указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"