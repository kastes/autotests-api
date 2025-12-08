import httpx

"""
1. Выполнить вход в систему.
2. Получить access-токен.
3. Получить информацию о текущем пользователе.
Перед выполнением должен быть запущен локальный сервер на порту 8000.
"""

login_payload = {"email": "user@gmail.com", "password": "password"}
print(
    'Выполнить запрос httpx.post("http://localhost:8000/api/v1/authentication/login",'
    " json=login_payload)"
)
login_resp = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
print(login_resp.status_code)

print()

access_token = login_resp.json()["token"]["accessToken"]
auth_header = {"Authorization": f"Bearer {access_token}"}
print('Выполнить запрос httpx.get("http://localhost:8000/api/v1/users/me", headers=auth_header)')
user_resp = httpx.get("http://localhost:8000/api/v1/users/me", headers=auth_header)
print(user_resp.status_code)
print(user_resp.json())
