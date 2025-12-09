import httpx
from httpx_example_tools import print_response

# Чтобы избежать зависаний, всегда указывайте timeout
try:
    response = httpx.get("https://postman-echo.com/delay/3", timeout=4)
    print_response(response)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")

print()

try:
    response = httpx.get("https://postman-echo.com/delay/3", timeout=2)
    print_response(response)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
