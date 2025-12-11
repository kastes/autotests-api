from httpx import Client

from clients import BASE_URL, TIMEOUT


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками для доступа к открытой части API.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(timeout=TIMEOUT, base_url=BASE_URL)
