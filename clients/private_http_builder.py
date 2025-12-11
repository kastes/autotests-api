from typing import TypedDict

from httpx import Client

from clients import BASE_URL, TIMEOUT
from clients.authentication.authentication_client import (
    LoginRequestDict,
    get_authentication_client,
)


class AuthenticationUserDict(TypedDict):
    """
    Описание структуры данных пользователя для аутентификации.
    """

    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Получить экземпляр httpx.Client с настройками для запросов к закрытой части API.

    :param user: Пользователь для которого будет получен доступ к закрытой части API.
    :type user: AuthenticationUserDict
    :return: httpx.Client для запросов к закрытой части API.
    :rtype: httpx.Client
    """
    authentication_client = get_authentication_client()
    login_request = LoginRequestDict(email=user["email"], password=user["password"])
    token_data = authentication_client.login(login_request)
    headers = {"Authorization": f"Bearer {token_data['token']['accessToken']}"}
    return Client(timeout=TIMEOUT, base_url=BASE_URL, headers=headers)
