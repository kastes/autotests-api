import httpx
from tools import print_response

print('Выполнить GET-запрос  httpx.get("https://jsonplaceholder.typicode.com/todos/1")')
resp = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print_response(resp)
print()

print('Выполнить POST-запрос  httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)')
print("Данные передаются как JSON в теле запроса")
data = {"userId": 1, "title": "Новое дело", "compltete": False}
resp = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print_response(resp)
print()


"""Важно! В некоторых примерах используется сервис httpbin.org для тестирования HTTP-запросов.
Иногда он может быть временно недоступен и возвращать ошибки вроде 503. В таком случае вы можете
 использовать альтернативный сервис — https://postman-echo.com,
   который полностью совместим с приведёнными примерами."""
print('Выполнить POST-запрос  httpx.post("https://postman-echo.com/post", data=data)')
print("Данные передаются как x-www-form-urlencoded в теле запроса")
data = {"username": "test_user", "password": "123456"}
# resp = httpx.post("https://httpbin.org/post", data=data)
resp = httpx.post("https://postman-echo.com/post", data=data)
print_response(resp)
print()

print("Передача заголовков")
print('Выполнить httpx.get("https://postman-echo.com/headers", headers=headers)')
headers = {"Authorization": "Bearer my-secret-token"}
# resp = httpx.post("https://httpbin.org/get", headers=headers)
resp = httpx.get("https://postman-echo.com/headers", headers=headers)
print_response(resp)
print()


print("Работа с параметрами запроса")
print('Выполнить httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)')
params = {"userId": 1}
resp = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print_response(resp)
print()
