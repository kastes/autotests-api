import pytest
from pydantic import BaseModel, EmailStr, SecretStr

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import (
    PrivateUsersClient,
    get_private_users_client,
)
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    """
    Данные запроса и ответа сценария 'создать пользователя'.
    """

    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> SecretStr:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура создаёт нового пользователя выполняя сценарий 'создать пользователя'.

    Args:
        public_users_client (PublicUsersClient): фикстура создаёт клиента доступа к открытой
        части API /api/v1/users.

    Returns:
        UserFixture: данные запроса и ответа сценария 'создать пользователя'.
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    """
    Фикстура создаёт клиента доступа к открытой части API /api/v1/users.

    Returns:
        PublicUsersClient: клиент доступа к открытой части API /api/v1/users.
    """
    return get_public_users_client()


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Фикстура создаёт клиента доступа к закрытой части API /api/v1/users
    пользователя созданного фикстурой function_user

    Args:
        function_user (UserFixture): фикстура создаёт нового пользователя

    Returns:
        PrivateUsersClient: клиент доступа к закрытой части API /api/v1/users
    """
    return get_private_users_client(function_user.authentication_user)
