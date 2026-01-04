"""
Проверки пользователя users
"""

import allure

from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
    UserSchema,
)
from tools.assertions.base import assert_equal


@allure.step("Check create user response")
def assert_create_user_response(
    request: CreateUserRequestSchema, response: CreateUserResponseSchema
) -> None:
    """
    Проверить данные ответа 'создать пользователя'

    Args:
        request (CreateUserRequestSchema): данные запроса 'создать пользователя'
        response (CreateUserResponseSchema): данные ответа 'создать пользователя'

    Raises:
        AssertionError: если данные ответа не соответствуют данным запроса
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


@allure.step("Check user")
def assert_user(expected: UserSchema, actual: UserSchema) -> None:
    """
    Проверить совпадение ожидаемых и действительных данных пользователя.

    Args:
        expected (UserSchema): ожидаемые данные пользователя
        actual (UserSchema): действительные данные пользователя

    Raises:
        AssertionError: если данные не равны
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")


@allure.step("Check get user response")
def assert_get_user_response(
    create_user_response: CreateUserResponseSchema, get_user_response: GetUserResponseSchema
) -> None:
    """
    Проверить данные ответа 'получить пользователя'

    Args:
        create_user_response (CreateUserResponseSchema): данные ответа 'создать пользователя'
        get_user_response (GetUserResponseSchema): данные ответа 'получить пользователя'

    Raises:
        AssertionError: если данные созданного пользователя
        не соответствуют данным полученного пользователя.
    """
    assert_user(create_user_response.user, get_user_response.user)
