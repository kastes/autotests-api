"""
Секретные данные в SecretStr. Как их получить.
"""

from pydantic import SecretStr

from clients.authentication.authentication_schema import LoginRequestSchema

login_schema = LoginRequestSchema(email="user@mail.com", password=SecretStr("password"))

print(f"{login_schema=}")
print()

print(f"{login_schema.model_dump()=}")
print()

print(f"{login_schema.model_dump_json()=}")
print()

print(f"{login_schema.model_dump(exclude={"password"})=}")
print()

print(f"{login_schema.password.get_secret_value()=}")
print()

login_dict = login_schema.model_dump(exclude={"password"})
print(login_dict, type(login_dict))
print()

login_dict["password"] = login_schema.password.get_secret_value()
print(login_dict, type(login_dict))
print()
