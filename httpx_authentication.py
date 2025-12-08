import httpx

"""
1. Выполнить вход в систему.
2. Обновить токен.
Перед выполнением должен быть запущен локальный сервер на порту 8000.
"""


login_payload = {"email": "user@gmail.com", "password": "password"}
print(
    'Выполнить запрос httpx.post("localhost:8000/api/v1/authentication/login", json=login_payload)'
)
login_resp = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
print(login_resp.status_code)
print(login_resp.json())

print()

refresh_token = login_resp.json()["token"]["refreshToken"]
refresh_payload = {"refreshToken": refresh_token}
print(
    'Выполнить запрос httpx.post("localhost:8000/api/v1/authentication/refresh",'
    " json=refresh_payload)"
)
refresh_resp = httpx.post(
    "http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload
)
print(refresh_resp.status_code)
print(refresh_resp.json())
