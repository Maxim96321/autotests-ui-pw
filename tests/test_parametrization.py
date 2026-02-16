import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -2])
def test_number(number: int):
    assert number > 0


@pytest.mark.parametrize('number , expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")
