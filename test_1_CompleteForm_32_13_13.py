'''
Задание: оформляем тесты в стиле unittest
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения.

Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestCompleteForm1(unittest.TestCase):

    def test_1_CompleteForm_32_13_13(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        wait = WebDriverWait(browser, 10)

        browser.get('http://suninjuly.github.io/registration1.html')

        inputFirstName = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        inputFirstName.send_keys('R')

        inputLastName = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        inputLastName.send_keys('S')

        inputEmail = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        inputEmail.send_keys('Email')

        inputPhone = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input')
        inputPhone.send_keys('555 55 55')

        inputAddress = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input')
        inputAddress.send_keys('Address')

        button = browser.find_element(By.XPATH, '/html/body/div/form/button')
        browser.execute_script('return arguments[0].scrollIntoView(true);', button)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/button')))
        button.click()

        welcomeText = browser.find_element(By.XPATH, '/html/body/div/h1')

        welcome_text = welcomeText.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "Should be absolute value of a number")
        browser.quit()

    def test_2_CompleteForm_32_13_13(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        wait = WebDriverWait(browser, 10)

        browser.get('http://suninjuly.github.io/registration2.html')

        inputFirstName = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        inputFirstName.send_keys('R')

        inputLastName = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        inputLastName.send_keys('S')

        inputEmail = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        inputEmail.send_keys('Email')

        inputPhone = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input')
        inputPhone.send_keys('555 55 55')

        inputAddress = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input')
        inputAddress.send_keys('Address')

        button = browser.find_element(By.XPATH, '/html/body/div/form/button')
        browser.execute_script('return arguments[0].scrollIntoView(true);', button)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/button')))
        button.click()

        welcomeText = browser.find_element(By.XPATH, '/html/body/div/h1')

        welcome_text = welcomeText.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text,
                         "Should be absolute value of a number")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
