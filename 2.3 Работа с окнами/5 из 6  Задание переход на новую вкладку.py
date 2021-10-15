'''
2.3 Работа с окнами
5 из 6 шагов пройдено
3 из 5 баллов  получено
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/redirect_accept.html')
button = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary')
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


solution = browser.find_element(By.CSS_SELECTOR, 'span.nowrap#input_value')
x = solution.text

inputSolution = browser.find_element(By.ID, 'answer')
inputSolution.send_keys(calc(x))

submit = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
submit.click()

'''
browser.switch_to.window(window_name)
Чтобы узнать имя новой вкладки, нужно использовать
метод window_handles, который возвращает массив имён
всех вкладок. Зная, что в браузере теперь открыто две
вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]
Также мы можем запомнить имя текущей вкладки,
чтобы иметь возможность потом к ней вернуться:

first_window = browser.window_handles[0]
'''
