from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса создания файла.
    upload_file - путь к загружаемому файлу.
    На сервере файл будет сохранён с именем filename в directory.
    """

    filename: str
    directory: str
    upload_file: str


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
