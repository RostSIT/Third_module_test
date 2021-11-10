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

link = "https://www.google.com/"

@pytest.mark.parametrize('element', ["/html/body/div[1]/div[2]/div/img", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"])
                                  # "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]/span", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]/svg/path[1]",
                                  # "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]/svg/path[1]", "https://stepik.org/lesson/236903/step/1",
                                  # "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]"])




class TestLogin:



    def test_guest_should_see_login_link(self, browser, element, en):
        browser.get(link)

        browser.implicitly_wait(10)

        inputAnswer = browser.find_element_by_xpath(element)
        assert inputAnswer == en, "Should google element"



# a = TestLogin()
# a.answer()
# a.test_guest_should_see_login_link()






# --------------------------------------------------


# element = ''
#
#
# def test_searchElements(browser):
#     browser.get(link)
#     browser.find_element_by_css_selector(element)
#
#
# def xxx():
#     element = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
#     json_response = requests.get(test_link + '/branches').json()
#     assert 4 == len(json_response)
#
#
# @pytest.mark.parametrize("expected_branches", ['dependabot/pip/docs/django-3.1.13',
#                                                'dependabot/pip/docs/pillow-8.3.2',
#                                                'develop',
#                                                'master'])
# def test_check_branches_names(expected_branches):
#     existing_branches_names = []
#     json_response = requests.get(test_link + '/branches').json()
#     for branch in json_response:
#         existing_branches_names.append((branch['name']))
#     assert expected_branches in existing_branches_names
#
