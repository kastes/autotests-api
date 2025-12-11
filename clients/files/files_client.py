from typing import ReadOnly, TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса создания файла.
    upload_file - путь к загружаемому файлу.
    На сервере файл будет сохранён с именем filename в directory.
    """

    filename: str
    directory: str
    upload_file: str


class File(TypedDict):
    id: str
    filename: str
    directory: str
    url: ReadOnly[str]


class CreateFileResponseDict(TypedDict):
    file: File


class FilesClient(APIClient):
    """
    Клиент для работы с API файлов /api/v1/files
    """

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Создать файл

        :param request: Данные для создания файла
        :type request: CreateFileRequestDict
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        with open(request["upload_file"], "rb") as upload_file:
            response = self.post("/api/v1/files", data=request, files={"upload_file": upload_file})
        return response

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        """
        Создать файл и вернуть данные в формате CreateFileResponseDict

        :param request: Данные для создания файла
        :type request: CreateFileRequestDict
        :return: Данные файла
        :rtype: CreateFileResponseDict
        """
        response = self.create_file_api(request)
        return response.json()

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


def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Создать экземпляр FilesClient с настройками доступа к закрытой части API для пользователя user.

    :param user: Данные пользователя для аутентификации
    :type user: AuthenticationUserDict
    :return: Готовый к использованию экземпляр FilesClient
    :rtype: FilesClient
    """
    return FilesClient(client=get_private_http_client(user=user))
