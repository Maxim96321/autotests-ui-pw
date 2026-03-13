import pytest


@pytest.mark.smoke
def test_smoke_case():
    ...


@pytest.mark.regression
def test_regression():
    ...

@pytest.mark.smoke
class TestSuit:
    def test_case1(self):
        ...

    def test_case2(self):
        ...
