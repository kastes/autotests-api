"""
Практикуемся в использовании API-клиентов.

1. Создать пользователя через API
2. Авторизовать пользователя
3. Получить его данные по /api/v1/users/{user_id}
"""

from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import (
    CreateUserRequestDict,
    get_public_users_client,
)
from tools.fakers import get_random_email

# 1 Создать пользователя через API
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string",
)
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_data = create_user_response.json()
print("User data: ", create_user_data)
print()

# 2 Авторизовать пользователя и получить клиент для доступа к закрытой части API.
authentication_user = AuthenticationUserDict(
    email=create_user_request["email"], password=create_user_request["password"]
)
private_users_client = get_private_users_client(user=authentication_user)

# 3 Получить данные пользователя по /api/v1/users/{user_id}
get_user_response = private_users_client.get_user_api(user_id=create_user_data["user"]["id"])
print("User data: ", get_user_response.json())
