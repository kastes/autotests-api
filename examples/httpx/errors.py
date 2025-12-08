import httpx

# Если API возвращает ошибку (код ответа не 2xx), можно вызвать raise_for_status(),
# чтобы вызвать исключение. Иначе raise_for_status() вернёт self.

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")
