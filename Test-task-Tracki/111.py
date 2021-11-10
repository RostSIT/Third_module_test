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


link = "https://github.com/Fantomas42/django-blog-zinnia"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    pullOpenRequestsLink = browser.find_element_by_css_selector("#pull-requests-repo-tab-count.Counter")
    pullOpenRequestsQuantity = pullOpenRequestsLink.text

    pullClosedRequestsLink = browser.find_element_by_css_selector('// *[ @ id = "repo-content-pjax-container"] / div / div[3] / div / a[2] '
                                             '/ svg')
    pullClosedRequestsQuantity = pullClosedRequestsLink.text

    r = requests.get('https://api.github.com/repos/torvalds/linux/pulls').text
    # len(r.json()) == int(count)
    print(f'\n{r}')
    print(f'\n{pullOpenRequestsQuantity}')
    print(f'\n{pullClosedRequestsQuantity}')

    c = requests.get('http://json-schema.org/draft-04/schema#').text
    print(f'\n{c}')
