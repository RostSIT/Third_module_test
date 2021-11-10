import requests
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





# # link = "https://github.com/Fantomas42/django-blog-zinnia"
test_link = "https://api.github.com/repos/Fantomas42/django-blog-zinnia"


def test_check_amount_of_pull_requests():
    json_response = requests.get(test_link+'/pulls').json()
    assert 9 == len(json_response)


def test_check_amount_of_branches():
    json_response = requests.get(test_link+'/branches').json()
    assert 4 == len(json_response)


@pytest.mark.parametrize("expected_branches", ['dependabot/pip/docs/django-3.1.13',
                                               'dependabot/pip/docs/pillow-8.3.2',
                                               'develop',
                                               'master'])
def test_check_branches_names(expected_branches):
    existing_branches_names = []
    json_response = requests.get(test_link + '/branches').json()
    for branch in json_response:
        existing_branches_names.append((branch['name']))
    assert expected_branches in existing_branches_names
#
#
# def test_check_amount_of_pull_requests(json_response = requests.get(test_link+'/pulls').json():
#     assert 9 == len(json_response)
#
# # def test_guest_should_see_login_link(browser):
# #     browser.get(link)
# #     pullOpenRequestsLink = browser.find_element_by_css_selector("#pull-requests-repo-tab-count.Counter")
# #     pullOpenRequestsQuantity = pullOpenRequestsLink.text
#
#     # pullClosedRequestsLink = browser.find_element_by_xpath('//*[@id="repo-content-pjax-container"]/div/div[3]/div/a[2]')
#     # pullClosedRequestsQuantity = pullClosedRequestsLink.text
#
#     r = requests.get('https://api.github.com/repos/torvalds/linux/pulls').text
#     # len(r.json()) == int(count)
#     print(f'\n{r}')
#     print(f'\n{pullOpenRequestsQuantity}')
#     print(f'\n{pullClosedRequestsQuantity}')
#
#     # c = requests.get('http://json-schema.org/draft-04/schema#').text
#     # print(f'\n{c}')
