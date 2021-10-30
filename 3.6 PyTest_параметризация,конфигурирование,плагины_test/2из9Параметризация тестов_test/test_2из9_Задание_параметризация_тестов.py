"""3.6 PyTest — параметризация, конфигурирование, плагины 4 из 9 шагов пройдено 3 из 8 баллов  получено Задание:
параметризация тестов Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы
смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест
со следующим сценарием действий:

открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
Опциональный фидбек — это текст в черном поле, как показано на скриншоте:


Правильным ответом на задачу в заданных шагах является число:

import time
import math

answer = math.log(int(time.time()))
Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:

https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты
работали стабильно.

В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со
строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.

Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время (
https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают. """

import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestLogin:

    def answer(self):
        self.answer = self.x
        self.a += self.answer
        print(self.a, self.x)

    def test_guest_should_see_login_link(self, browser, link, ):
        browser.get(link)
        answer = math.log(int(time.time()))
        print('\n', answer)

        browser.implicitly_wait(10)

        inputAnswer = browser.find_element_by_css_selector('div[data-state="no_submission"] textarea')
        inputAnswer.send_keys(str(math.log(int(time.time()))))

        sendButton = browser.find_element_by_css_selector('button[class="submit-submission"]')
        sendButton.click()

        xEl = browser.find_element(By.CSS_SELECTOR, 'pre[class="smart-hints__hint"]')
        self.x = xEl.text
        self.a = ''
        self.a += self.x
        print('\n', self.a, self.x)
        assert self.x == 'Correct!', \
            f'expected {self.a}, {self.x}'


a = TestLogin()
a.answer()
a.test_guest_should_see_login_link()




