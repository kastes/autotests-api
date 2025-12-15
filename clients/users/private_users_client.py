from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema


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

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Получить пользователя с идентификатором user_id и вернуть его данные

        :param user_id: Идентификатор пользователя
        :type user_id: str
        :return: Данные пользователя
        :rtype: GetUserResponseSchema
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Обновить данные пользователя с идентификатором user_id

        :param user_id: Идентификатор пользователя
        :type user_id: str
        :param request: Данные пользователя для обновления
        :type request: UpdateUserRequestSchema
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Удалить пользователя с идентификатором user_id

        :param user_id: Идентификатор пользователя
        :type user_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Создать экземпляр PrivateUsersClient с настройками доступа к закрытой части API
      для пользователя user.

    :param user: Данные пользователя для аутентификации
    :type user: AuthenticationUserSchema
    :return: Готовый к использованию экземпляр PrivateUsersClient
    :rtype: PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user=user))
