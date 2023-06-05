import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

#обработчик, позволяющий считывать опцию --language с командной строки
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language of interface")
    
@pytest.fixture(scope="class")
def browser(request):

    user_language = request.config.getoption("language") #считываем язык, который прописываем в терминале
    browser = None

    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) #язык, используемый при открытии браузера

    if user_language: #если язык в терминале при запуске теста указан, то браузер открывается
        print("start testing")
        browser = webdriver.Chrome(options=options)
        sleep(5)
    else:
        print("Нужно ввести язык")

    yield browser
    print("\nquit browser..")
    sleep(5)
    browser.quit()