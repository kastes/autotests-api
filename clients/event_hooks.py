import allure
import httpx

from tools.http.curl import make_curl_from_request


def curl_event_hook(request: httpx.Request) -> None:
    """
    Прикрепить curl-команду к Allure-отчёту

    Args:
        request (httpx.Request): запрос, который передаётся в httpx клиент
    """
    curl_command = make_curl_from_request(request)
    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)
