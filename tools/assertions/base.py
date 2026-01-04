"""
Базовые проверки
"""

from typing import Any, Sized

import allure


@allure.step("Check that response status code equals {expected}")
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


@allure.step("Check that {name} equals {expected}")
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


@allure.step("Check that {name} is True")
def assert_is_true(actual: Any, name: str) -> None:
    """
    Проверить значение на истинность
    Args:
        actual (Any): Значение для проверки
        name (str): Имя
    Raises:
        AssertionError: если значение не приводится к True
    """
    assert actual, f"Имя: {name}. Ожидался: {True}. Получен {actual}"


def assert_length(actual: Sized, expected: Sized, name: str) -> None:
    """
    Проверить объекты на равенство длины

    :param actual: фактический объект
    :type actual: Sized
    :param expected: ожидаемый объект
    :type expected: Sized
    :param name: имя объекта
    :type name: str
    :raises AssertionError: если длины объектов не совпадают
    """
    with allure.step(f"Check that length of {name} equals {len(expected)}"):
        assert len(actual) == len(expected), (
            f"Имя: {name}. Длины ожидаемого и полученного объектов не совпадают. "
            f"Ожидалось: {len(expected)}. Получено: {len(actual)}"
        )
