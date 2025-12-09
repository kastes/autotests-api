import httpx

from tools.fakers import get_random_email

# Create user
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}

create_user_resp = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_data = create_user_resp.json()
print(create_user_resp.url, "->", create_user_resp.status_code)
print(create_user_data)
print()

# Login user
login_user_payload = {"email": create_user_data["user"]["email"], "password": "string"}
login_user_resp = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=login_user_payload
)
login_user_data = login_user_resp.json()
print(login_user_resp.url, "->", login_user_resp.status_code)
print(login_user_data)
print()

# Update user
update_user_headers = {"Authorization": f"Bearer {login_user_data["token"]["accessToken"]}"}
update_user_payload = {
    "email": get_random_email(),
    "lastName": "Update string",
    "middleName": "Update middle",
}
update_user_resp = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_data["user"]["id"]}",
    headers=update_user_headers,
    json=update_user_payload,
)
update_user_data = update_user_resp.json()
print(update_user_resp.url, "->", update_user_resp.status_code)
print(update_user_data)
