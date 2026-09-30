import pytest

pytestmark = pytest.mark.skip("Пропустить примеры тестов.")


def test_pytest_first() -> None:
    pass


def test_pytest_second() -> None:
    assert False


def test_pytest_third() -> None:
    assert True


class TestPytestClass:
    def test_method_one(self) -> None:
        pass

    def test_method_two(self) -> None:
        pass


def test_exceptions() -> None:
    with pytest.raises(ZeroDivisionError):
        1 / 0  # pyright: ignore[reportUnusedExpression] # noqa: B018


def test_lists():
    assert [1, 2, 3] == [1, 2, 4]
