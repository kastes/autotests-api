"""
Валидируем ответы API
"""

from jsonschema import ValidationError, validate
from pydantic import BaseModel, SecretStr

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password=SecretStr("TOP SECRET PASSWORD"),
    lastName="C",
    middleName="F",
    firstName="J",
)
create_user_response = public_users_client.create_user_api(create_user_request)

create_user_response_json = create_user_response.json()
print(create_user_response_json)
print()

print(CreateUserRequestSchema.model_json_schema())
print()


# Проверяем экземпляр ответа по схеме запроса и валидация проходит!
# Потому что у запросов все поля со значениями по умолчанию не
# включаются в схеме список обязательных! А дополнительные поля не дают ошибки!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Проверять схему надо только по данным ответа от сервера,
# в схемах ответов нет значений по умолчанию и все поля обязательные!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
validate(create_user_response_json, CreateUserRequestSchema.model_json_schema())

validate_json_schema(
    instance=create_user_response_json, schema=CreateUserRequestSchema.model_json_schema()
)
print("Ok")
print()


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

print()


# Дополнительные данные в экземпляре не дают ошибку при валидации!!!
class MyModel(BaseModel):
    a: int
    b: str
    d: str


# Входные данные в виде строки (поле "a" задано строкой, а не числом)
# Проверять схему надо только по данным ответа от сервера,
# в схемах ответов нет значений по умолчанию и все поля обязательные!
print("Дополнительные данные в экземпляре не дают ошибку при валидации!!!")
print(f"{MyModel.model_json_schema()=}")
data = {"a": 1, "b": "Hello!", "c": "c", "d": "d"}
data_json = '{"a": "1", "b": "Hello!", "d": "d", "c": "c"}'
print(f"{data_json=}")
my_model = MyModel.model_validate_json(data_json)  # Ошибки не будет

print(
    f"{MyModel.model_validate_json(data_json)=}"
)  # Выведет: a=1 b='Hello!, d='d' , c не будет учтено!!

print(f"{data=}")
print(f"{validate(data, MyModel.model_json_schema())=}")  # type: ignore
validate(data, MyModel.model_json_schema())
print("Done OK")
