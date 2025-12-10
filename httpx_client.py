import httpx

login_payload = {"email": "user@gmail.com", "password": "password"}

login_resp = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_data = login_resp.json()
access_token = login_data["token"]["accessToken"]
print(login_data)
print()

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=10,
    headers={"Authorization": f"Bearer {access_token}"},
)
resp_users_me = client.get(
    "/api/v1/users/me",
)
print(resp_users_me.status_code, resp_users_me.text, resp_users_me.headers)
