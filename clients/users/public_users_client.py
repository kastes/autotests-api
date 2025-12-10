from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса создания пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с открытой частью API пользователей /api/v1/users.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создаёт нового пользователя

        :param request: Данные для создания нового пользователя
        :type request: CreateUserDict
        :return: Ответ сервера
        :rtype: Response
        """
        return self.post("/api/v1/users", json=request)
