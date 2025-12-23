import pytest

from clients.authentication.authentication_client import (
    AuthenticationClient,
    get_authentication_client,
)


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    """
    Фикстура создаёт клиента работы с API аутентификации /api/v1/authentication.

    Returns:
        AuthenticationClient: клиент работы с API аутентификации /api/v1/authentication.
    """
    return get_authentication_client()
