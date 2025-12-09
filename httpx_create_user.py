import httpx

from tools.fakers import get_random_email

create_user_json = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}

create_user_resp = httpx.post("http://localhost:8000/api/v1/users", json=create_user_json)

print(create_user_resp.status_code)
print(create_user_resp.json())
