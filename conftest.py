"""3.6 PyTest — параметризация, конфигурирование, плагины 4 из 9 шагов пройдено 3 из 8 баллов  получено Conftest.py —
конфигурация тестов Ранее мы добавили фикстуру browser, которая создает нам экземпляр браузера для тестов в данном
файле. Когда файлов с тестами становится больше одного, приходится в каждом файле с тестами описывать данную
фикстуру. Это очень неудобно. Для хранения часто употребимых фикстур и хранения глобальных настроек нужно
использовать файл conftest.py, который должен лежать в директории верхнего уровня в вашем проекте с тестами. Можно
создавать дополнительные файлы conftest.py в других директориях, но тогда настройки в этих файлах будут применяться
только к тестам в под-директориях.

Создадим файл conftest.py в корневом каталоге нашего тестового проекта и перенесем туда фикстуру browser. Заметьте,
насколько лаконичнее стал выглядеть файл с тестами.
"""

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

"""Теперь, сколько бы файлов с тестами мы ни создали, у тестов будет доступ к фикстуре browser. Фикстура передается в 
тестовый метод в качестве аргумента. Таким образом можно удобно переиспользовать одни и те же вспомогательные функции 
в разных частях проекта. """
