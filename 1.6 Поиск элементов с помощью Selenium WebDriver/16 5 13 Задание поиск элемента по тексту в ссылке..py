import math
import time
from selenium import webdriver

browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/find_link_text')
    Link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    Link.click()
    inputName = browser.find_element_by_name('first_name')
    inputName.send_keys('Ruslan')
    inputLastName = browser.find_element_by_name('last_name')
    inputLastName.send_keys('Pratsko')
    inputCity = browser.find_element_by_class_name('form-control.city')
    inputCity.send_keys('Kuiv')
    inputCountry = browser.find_element_by_id('country')
    inputCountry.send_keys('ua')
    button = browser.find_element_by_class_name('btn.btn-default')
    button.click()

finally:

    time.sleep(30)
    browser.quit()
