#Базовая страница, от которой будут унаследованы все остальные классы.
#Опишем вспомогательне методы для  работы с драйвером
#здесь инициализируем атрибуты объекта
#создаем метод открытия страницы
#создаем метод перехвата исключений
from selenium.common.exceptions import NoSuchElementException

class BasePage():

    #browser = webdriver.Chrome(options=options)
    #url = ''
    #self = объект page
    def __init__(self, browser, url, timeout=10):
        self.browser = browser #экземпляр драйвера
        self.url = url #url-адрес
                        #как атрибуты объекта, с которыми работаем в методах
        #команда для неявного ожидания
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    #метод для перехвата исключений
    #здесь два аргумента: как(css, id, xpath и тд) и что(строку-селектор) искать
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
