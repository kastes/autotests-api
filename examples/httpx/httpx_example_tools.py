import httpx


def print_response(resp: httpx.Response) -> None:
    print(f"{resp.url=}")
    print(f"{resp.status_code}")
    print(resp.json())
