from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')
button = browser.find_element_by_xpath('/html/body/form/div/div/button')
button.click()

alert = browser.switch_to.alert
alert.accept()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_el = browser.find_element_by_css_selector('span.nowrap#input_value')
x = x_el.text

inputSolution = browser.find_element_by_xpath('//*[@id="answer"]')
inputSolution.send_keys(calc(x))

submit = browser.find_element_by_xpath('/html/body/form/div/div/button')
submit.click()

# Чтобы получить текст из alert, используйте свойство text объекта alert:
# alert = browser.switch_to.alert
# alert_text = alert.text

'''
Другой вариант модального окна, который предлагает пользователю выбор 
согласиться с сообщением или отказаться от него, называется confirm. 
Для переключения на окно confirm используется та же команда, 
что и в случае с alert:
'''

# confirm = browser.switch_to.alert
# confirm.accept()

# Для confirm-окон можно использовать следующий метод для отказа:
# confirm.dismiss()
# То же самое, что и при нажатии пользователем кнопки "Отмена".

'''
Третий вариант модального окна — prompt — имеет 
дополнительное поле для ввода текста. Чтобы ввести текст, 
используйте метод send_keys():
'''

# prompt = browser.switch_to.alert
# prompt.send_keys('My answer')
# prompt.accept()
time.sleep(60)
browser.quit()
