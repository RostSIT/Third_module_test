import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False


"""
3.5 PyTest — маркировка 6 из 7 шагов пройдено 1 из 2 баллов  получен Задание: пропуск тестов Изучите 
самостоятельно документацию про маркировку xfail. Найдите там параметр, который в случае неожиданного прохождения 
теста, помеченного как xfail, отметит в отчете этот тест как упавший. Пометьте таким образом первый тест из этого 
тестового набора. 

test_xfail.py:

import pytest


def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip def test_skipped(): assert False Запустите полученные тесты. Обратите внимание на статус прогона 
тестов. Найдите последнюю строчку с итогами запуска, скопируйте текст между символами === и отправьте его в качестве 
ответа на это задание. 
"""