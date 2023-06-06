#в этом файле будут храниться селекторы
#делаем это для того, чтобы хранить каждый селектор во внешней переменной
#каждый класс здесь будет соответствовать каждому классу PageObject

from selenium.webdriver.common.by import By

#класс с локаторами для класса MainPage()
class MainPageLocators():
    #теперь каждый селектор будет парой: как и что искать
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
