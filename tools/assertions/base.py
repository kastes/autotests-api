"""
Базовые проверки
"""

from typing import Any


def assert_status_code(actual: int, expected: int) -> None:
    """
    Проверить кода ответа на соответствие ожидаемому

    :param actual: действительный код ответа
    :type actual: int
    :param expected: ожидаемый код ответа
    :type expected: int
    :raises AssertionError: если коды не совпадают
    """
    assert actual == expected, f"Неправильный код ответа. Ожидался: {expected}. Получен {actual}"


def assert_equal(actual: Any, expected: Any, name: str) -> None:
    """
    Проверить действительное значение на равенство ожидаемому

    :param actual: действительное значение
    :type actual: Any
    :param expected: ожидаемое значение
    :type expected: Any
    :raises AssertionError: если значения не равны
    """
    assert actual == expected, f"Имя: {name}. Ожидался: {expected}. Получен {actual}"


def assert_is_true(actual: Any, name: str) -> None:
    """
    Проверить значение на истинность

    Args:
        actual (Any): Значение для проверки
        name (str): Имя
    Raises AssertionError: если значение не приводится к True
    """
    assert actual, f"Имя: {name}. Ожидался: {True}. Получен {actual}"
