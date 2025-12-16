"""
Секретные данные в SecretStr. Как их получить.
"""

import uuid

from pydantic import SecretStr

from clients.authentication.authentication_schema import LoginRequestSchema
from clients.courses.courses_schema import UpdateCourseRequestSchema
from clients.users.users_schema import UserSchema

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


user = UserSchema(
    id=uuid.uuid4(), email="user@mail.com", lastName="C", firstName="J", middleName="F"
)
print(f"{user=}")
print(f"{user.model_dump()=}")
print(f"{user.model_dump_json()=}")
print(f"{user.id=}")
print(f"{str(user.id)=}")
print(f"{user.model_dump(mode='json')=}")
print()


update_request = UpdateCourseRequestSchema(title="title")
print(f"{update_request=}")
print(f"{update_request.model_dump()=}")
print(f"{update_request.model_dump(mode='json')=}")
print(f"{update_request.model_dump_json()=}")
print(f"{update_request.model_dump(mode='json')=}")
print()
