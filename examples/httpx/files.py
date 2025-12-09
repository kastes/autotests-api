from pathlib import Path

import httpx
from httpx_example_tools import print_response

print("Отправка файлов")
print('Выполнить httpx.post("https://postman-echo.com/post", files=files)')
with open(Path(__file__).parent / "pytest-logo.png", "rb") as upload_file:
    files = {"file": upload_file}
    resp = httpx.post("https://postman-echo.com/post", files=files)
print_response(resp)
print()
