import httpx
from tools import print_response

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print_response(response1)  # Данные первой задачи
print()
print_response(response2)  # Данные второй задачи
print()

print("Передача заголовков")
client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://postman-echo.com/headers")
print_response(response)  # Заголовки включены в ответ
client.close()
