"""
Проверки пользователя users
"""

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(
    request: CreateUserRequestSchema, response: CreateUserResponseSchema
) -> None:
    """
    Проверить данные ответа создать пользователя на соответствие запросу

    Args:
        request (CreateUserRequestSchema): данные запроса создать пользователя
        response (CreateUserResponseSchema): данные ответа создать пользователя

    Raises:
        AssertionError: если данные ответа не соответствуют данным запроса
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")
