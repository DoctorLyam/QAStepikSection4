#Базовая страница, от которой будут унаследованы все остальные классы.
#Опишем вспомогательне методы для  работы с драйвером

class BasePage():

    #browser = webdriver.Chrome(options=options)
    #url = ''
    #self = объект page
    def __init__(self, browser, url):
        self.browser = browser #экземпляр драйвера
        self.url = url #url-адрес
                        #как атрибуты объекта, с которыми работаем в методах
    
    def open(self):
        self.browser.get(self.url)
