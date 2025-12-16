"""
Валидируем ответы API
"""

from jsonschema import ValidationError, validate
from pydantic import SecretStr

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password=SecretStr("TOP SECRET PASSWORD"),
    lastName="C",
    middleName="F",
    firstName="J",
)
create_user_response = public_users_client.create_user_api(create_user_request)

create_user_response_json = create_user_response.json()
print(create_user_response_json)
# испортить поле email
create_user_response_json["user"]["email"] = "asd"
print(create_user_response_json)
print()

print(f"{CreateUserResponseSchema.model_json_schema()=}")
print()


# для валидации специальных форматов строк надо дополнительные действия
# здесь не ловится испорченный email
validate(instance=create_user_response_json, schema=CreateUserResponseSchema.model_json_schema())
print("Ok")
print()

# валидация вынесена в validate_json_schema - фасад, обёртка для доступа к библиотеке jsonschema
try:
    validate_json_schema(
        instance=create_user_response_json, schema=CreateUserResponseSchema.model_json_schema()
    )
    print("Ok")
except ValidationError as e:
    print(e)
