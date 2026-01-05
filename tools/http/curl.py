from httpx import Request, RequestNotRead


def make_curl_from_request(request: Request) -> str:
    """
    Создать строку curl-команды из запроса httpx.Request

    Args:
        request (Request): запрос httpx.Request

    Returns:
        str: Строка curl-команды с методом, URL, заголовками, телом запроса
             (если тело есть и данные тела не являются потоком)
    """
    curl_line = [f"curl -X '{request.method}'", f"'{request.url}'"]

    for header, value in request.headers.items():
        curl_line.append(f"-H '{header}: {value}'")

    try:
        if body := request.content:
            curl_line.append(f"-d '{body.decode("utf-8")}'")
    except RequestNotRead:
        curl_line.append("-d 'RequestNotRead'")

    return " \\\n ".join(curl_line)
