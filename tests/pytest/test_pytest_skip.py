import pytest


@pytest.mark.skip(reason='Фича в разработке')
def test_skip():
    ...

@pytest.mark.skip
class TestSuitSkip:
    def test_skip_1():
        ...

    def test_ski_2():
        ...
