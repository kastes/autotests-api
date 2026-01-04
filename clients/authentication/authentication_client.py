import allure
from httpx import Response

from clients.api_client import APIClient
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
    RefreshRequestSchema,
)
from clients.clients_tools import request_with_secret_to_dict
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    """
    Клиент для работы с аутентификацией /api/v1/authentication
    """

    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Выполнить аутентификацию пользователя

        :param request: Данные аутентификации пользователя
        :type request: LoginRequestSchema
        :return: Ответ от сервера httpx.Response
        """
        # request.model_dump(by_alias=True, exclude={"password"})
        # request_dict["password"] = request.password.get_secret_value()
        request_dict = request_with_secret_to_dict(request, secret_fields={"password"})
        return self.post("/api/v1/authentication/login", json=request_dict)

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Выполнить  аутентификацию пользователя и получить данные аутентификации

        :param request: Данные аутентификации пользователя
        :type request: LoginRequestSchema
        :return: Данные токена аутентификации
        :rtype: LoginResponseSchema
        """
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Обновление токена доступа пользователя

        :param request: Данные обновления токена пользователя
        :type request: RefreshRequestSchema
        :return: Ответ от сервера httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
