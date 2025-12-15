from httpx import Client
from pydantic import BaseModel, EmailStr, SecretStr

from clients import BASE_URL, TIMEOUT
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    """
    Описание структуры данных пользователя для аутентификации.
    """

    email: EmailStr
    password: SecretStr


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Получить экземпляр httpx.Client с настройками для запросов к закрытой части API.

    :param user: Пользователь для которого будет получен доступ к закрытой части API.
    :type user: AuthenticationUserDict
    :return: httpx.Client для запросов к закрытой части API.
    :rtype: httpx.Client
    """
    authentication_client = get_authentication_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    token_data = authentication_client.login(login_request)
    headers = {"Authorization": f"Bearer {token_data.token.access_token}"}
    return Client(timeout=TIMEOUT, base_url=BASE_URL, headers=headers)
