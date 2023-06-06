#в этом файле будут храниться селекторы
#делаем это для того, чтобы хранить каждый селектор во внешней переменной
#каждый класс здесь будет соответствовать каждому классу PageObject

from selenium.webdriver.common.by import By

#класс с локаторами для класса MainPage()
class MainPageLocators():
    #теперь каждый селектор будет парой: как и что искать
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

#класс с селекторами для страницы с логином и регистрацией для класса LoginPage()
class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")