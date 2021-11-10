import time
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


link = 'https://github.com/Fantomas42/django-blog-zinnia'


class TestProductPage:

    def test_button_add_to_basket_is_visible(self, browser):
        """Тест проверяет, что страница товара
         содержит кнопку добавления в корзину
        """
        # Открываем страницу товара
        browser.get(link)

        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
        time.sleep(5)

        # Проверяем наличие кнопки добавления товара в корзину
        assert browser.find_element_by_css_selector("button.btn-add-to-basket")
