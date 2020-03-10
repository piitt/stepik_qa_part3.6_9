import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# добавляем опцию --language в pytest
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help='Choose language: en-gb, es, fr, ru, uk, it, de, pt and others')


@pytest.fixture(scope='function')
def browser(request):
    # получаем значение опции --language
    lang = request.config.getoption('language')
    # создаем объект с опциями
    options = Options()
    # применяем опцию выбор языка
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    # запускаем браузер с опциями
    browser = webdriver.Chrome(options=options)
    print('\nstart chrome browser for test..', 'language =', lang)
    browser.maximize_window()
    yield browser
    # закрываем браузер
    print('\nquit browser..')
    browser.quit()
