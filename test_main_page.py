from selenium.webdriver.common.by import By
#импорт файла с методом нахождения кнопки на странице и кликом
from .pages.main_page import MainPage

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