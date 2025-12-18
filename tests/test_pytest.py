import pytest


def test_pytest_first() -> None:
    pass


def test_pytest_second() -> None:
    assert 1 == 2


def test_pytest_third() -> None:
    assert 1 == 1


class TestPytestClass:
    def test_method_one(self) -> None:
        pass

    def test_method_two(self) -> None:
        pass


def test_exceptions() -> None:
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_lists():
    assert [1, 2, 3] == [1, 2, 4]
