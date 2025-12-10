from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """

    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
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

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Обновление токена доступа пользователя

        :param request: Словать {"refreshToken": "str"}
        :return: Ответ от сервера httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)
