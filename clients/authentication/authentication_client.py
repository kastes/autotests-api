from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса аутентификации.
    """

    email: str
    password: str


class Token(TypedDict):
    """
    Описание структуры токена аутентификации.
    """

    tokenType: str
    accessToken: str
    refreshToken: str


class LoginResponseDict(TypedDict):  # Добавили структуру ответа аутентификации
    """
    Описание структуры ответа аутентификации.
    """

    token: Token


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса обновления токена.
    """

    refreshToken: str


class AuthenticationClient(APIClient):
    """
    Клиент для работы с аутентификацией /api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Выполняет аутентификацию пользователя

        :param request: Словать {"email": "str_email", "password": "str"}
        :return: Ответ от сервера httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        Docstring for login

        :param request: Данные аутентификации пользователя
        :type request: LoginRequestDict
        :return: Данные токена аутентификации
        :rtype: LoginResponseDict
        """
        response = self.login_api(request)
        return response.json()

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Обновление токена доступа пользователя

        :param request: Словать {"refreshToken": "str"}
        :return: Ответ от сервера httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)


def get_autentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
