from typing import Any

import allure
from httpx import URL, Client, Response
from httpx._types import QueryParamTypes, RequestData, RequestFiles


class APIClient:
    """
    Базовый API клиент, агрегирующий объект httpx.Client.
    """

    def __init__(self, client: Client):
        """
        Инициализация объекта

        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self._client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParamTypes | None = None) -> Response:
        """
        Выполнить GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :return: Объект Response с данными ответа.
        """
        return self._client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
    ) -> Response:
        """
        Выполнить POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
        :param files: Файлы для загрузки на сервер.
        :return: Объект Response с данными ответа.
        """
        return self._client.post(url, json=json, data=data, files=files)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Выполнить PATCH-запрос (частичное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self._client.patch(url, json=json)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        Выполнить DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :return: Объект Response с данными ответа.
        """
        return self._client.delete(url)
