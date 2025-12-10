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

# Create file
create_file_headers = {"Authorization": f"Bearer {login_user_data["token"]["accessToken"]}"}
create_file_payload = {
    "filename": "image.png",
    "directory": "directory",
    "upload_file": "./testdata/files/bart.png",
}
with open("./testdata/files/bart.png", "rb") as upload_file:
    create_file_resp = httpx.post(
        "http://localhost:8000/api/v1/files",
        headers=create_file_headers,
        data=create_file_payload,
        files={"upload_file": upload_file},
    )
create_file_data = create_file_resp.json()
print(create_file_resp.url, "->", create_file_resp.status_code)
print(create_file_data)
