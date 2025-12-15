from httpx import Response

from clients.api_client import APIClient
from clients.clients_tools import request_with_secret_to_dict
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Клиент для работы с открытой частью API пользователей /api/v1/users.
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создать нового пользователя

        :param request: Данные для создания нового пользователя
        :type request: CreateUserRequestSchema
        :return: Ответ сервера
        :rtype: Response
        """
        # request_dict = request.model_dump(by_alias=True, exclude={"password"})
        # request_dict["password"] = request.password.get_secret_value()
        request_dict = request_with_secret_to_dict(request, secret_fields={"password"})
        return self.post("/api/v1/users", json=request_dict)

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Создать нового пользователя и получить данные пользователя

        :param request: Данные для создания нового пользователя
        :type request: CreateUserRequestShema
        :return: Данные пользователя
        :rtype: CreateUserResponseSchema
        """
        response = self.create_user_api(request=request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """

    return PublicUsersClient(client=get_public_http_client())
