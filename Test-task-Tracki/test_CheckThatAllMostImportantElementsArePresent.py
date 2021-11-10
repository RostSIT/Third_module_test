import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="module")
def open_test_page(browser):
    browser.get("https://www.google.com/")
    browser.implicitly_wait(10)
    return browser


@pytest.mark.parametrize('element', ["/html/body/div[1]/div[2]/div/img", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input",
                                     "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]/span", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]/svg/path[1]",
                                     "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]/svg/path[1]", "https://stepik.org/lesson/236903/step/1",
                                     "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]"])
def test_check_google_main_page(open_test_page, element):
    assert open_test_page.find_element_by_xpath(element).is_displayed(), "Element was not found"
