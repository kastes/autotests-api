from httpx import Response

from clients.api_client import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)


class FilesClient(APIClient):
    """
    Клиент для работы с API файлов /api/v1/files
    """

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Создать файл

        :param request: Данные для создания файла
        :type request: CreateFileRequestSchema
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        with open(request.upload_file, "rb") as upload_file:
            response = self.post(
                "/api/v1/files",
                data=request.model_dump(by_alias=True, exclude={"upload_file"}),
                files={"upload_file": upload_file},
            )
        return response

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Создать файл и вернуть данные в формате CreateFileResponseSchema

        :param request: Данные для создания файла
        :type request: CreateFileRequestSchema
        :return: Данные файла
        :rtype: CreateFileResponseSchema
        """
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)

    def get_file_api(self, file_id: str) -> Response:
        """
        Получить файл с идентификатором file_id

        :param file_id: Идентификатор файла
        :type file_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def delete_file_api(self, file_id: str) -> Response:
        """
        Удалить файл с идентификатором file_id

        :param file_id: Идентификатор файла
        :type file_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Создать экземпляр FilesClient с настройками доступа к закрытой части API для пользователя user.

    :param user: Данные пользователя для аутентификации
    :type user: AuthenticationUserSchema
    :return: Готовый к использованию экземпляр FilesClient
    :rtype: FilesClient
    """
    return FilesClient(client=get_private_http_client(user=user))
