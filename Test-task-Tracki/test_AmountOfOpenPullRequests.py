import requests
import pytest


test_link = "https://api.github.com/repos/Fantomas42/django-blog-zinnia"


def test_check_amount_of_pull_requests():
    json_response = requests.get(test_link+'/pulls?accept=application/vnd.github.v3+json').json()
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
