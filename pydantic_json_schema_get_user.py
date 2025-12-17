from pydantic import SecretStr, ValidationError

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

# 1 создать нового пользователя
public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password=SecretStr("TOP SECRET PASSWORD"),
    lastName="C",
    middleName="F",
    firstName="J",
)
create_user = public_users_client.create_user(create_user_request)

# 2 получить пользователя по user_id
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email, password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)
get_user_response = private_users_client.get_user_api(str(create_user.user.id))


# 3 провалидровать ответ API
try:
    validate_json_schema(get_user_response.json(), GetUserResponseSchema.model_json_schema())
    print("Validation Ok")
except ValidationError as e:
    print(e)
