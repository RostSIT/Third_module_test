"""3.4 Использование фикстур в PyTest 6 из 7 шагов пройдено 0 из 1 баллa  получено Область видимости scope Для
фикстур можно задавать область покрытия фикстур. Допустимые значения: “function”, “class”, “module”, “session”.
Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, один раз для модуля или
один раз для всех тестов, запущенных в данной сессии.

Запустим все наши тесты из класса TestMainPage1 в одном браузере для экономии времени, задав scope="class" в фикстуре
browser:

test_fixture5.py
"""

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")