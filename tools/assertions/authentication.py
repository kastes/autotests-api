import allure

from clients.authentication.authentication_schema import (
    LoginResponseSchema,
)
from tools.assertions.base import assert_equal, assert_is_true


@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema) -> None:
    """
    Проверить данные ответа сценария 'успешная аутентификация пользователя'

    Args:
        response (LoginResponseSchema): данные ответа

    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым
    """
    assert_equal(response.token.token_type, "bearer", "token_type")
    assert_is_true(response.token.access_token, "access_token")
    assert_is_true(response.token.refresh_token, "refresh_token")
