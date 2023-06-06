#файл реализации методов проверки страницы

from selenium.webdriver.common.by import By
#импорт файла с методом нахождения кнопки на странице и кликом
from .pages.main_page import MainPage
#реализуем переход на страницу с логином (СПОСОБ 2)
from .pages.login_page import LoginPage

#вместо этого

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

#пишем теперь:
#напомню, что драйвер browser описали в coftest.py
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #создаем объект page c двумя атрибутами: вебдрайвер и ссылка
    #обращаемся к классу MainPage, т.к. он наследник BasePage,
    #в котором атрибуты класса browser, url инициализируются
    page = MainPage(browser, link)
    #вызываем метод открытия страницы из BasePage
    page.open()
    #вызываем метод поиска элемента и клика из наследника BasePage
    page.go_to_login_page()

    #ПЕРЕХОД МЕЖДУ СТРАНИЦАМИ (СПОСОБ 1):
    #login_page = page.go_to_login_page() -вместо просто page.go_to_login_page() присваиваем объект переменной
    #login_page.should_be_login_page()
    #, где присваиваем переменной объект с методом клика и перехода на другую страницу (из файла main_page.py),
    # а потом вызываем метод из LoginPage(BasePage), который вызывает три метода с проверками полей

    #ПЕРЕХОД МЕЖДУ СТРАНИЦАМИ (СПОСОБ 2):
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

#добавлю новый кейс с другим методом из MainPage -
#проверка наличия ссылки
def test_guest_should_see_login_link(browser):
    #снова объявляем ссылку, создаем объект, открываем страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    #но здксь используем другой метод - провернку наличия ссылки
    page.should_be_login_link()