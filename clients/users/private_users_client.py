from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса обновления пользовтеля
    """

    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class User(TypedDict):
    """
    Описание структуры пользователя.
    """

    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class GetUserResponseDict(TypedDict):
    """
    Описание структуры данных ответа получения пользователя.
    """

    user: User


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с закрытой частью API пользователей /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Получить текущего пользователя

        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить пользователя с идентификатором user_id

        :param user_id: Идентификатор пользователя
        :type user_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseDict:
        """
        Получить пользователя с идентификатором user_id и вернуть его данные

        :param user_id: Идентификатор пользователя
        :type user_id: str
        :return: Данные пользователя
        :rtype: GetUserResponseDict
        """
        response = self.get_user_api(user_id)
        return response.json()

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Обновить данные пользователя с идентификатором user_id

        :param user_id: Идентификатор пользователя
        :type user_id: str
        :param request: Данные пользователя для обновления
        :type request: UpdateUserRequestDict
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Удалить пользователя с идентификатором user_id

        :param user_id: Идентификатор пользователя
        :type user_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")


def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Создать экземпляр PrivateUsersClient с настройками доступа к закрытой части API
      для пользователя user.

    :param user: Данные пользователя для аутентификации
    :type user: AuthenticationUserDict
    :return: Готовый к использованию экземпляр PrivateUsersClient
    :rtype: PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user=user))
