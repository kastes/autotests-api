import uuid
from typing import TypedDict

from pydantic import BaseModel, ConfigDict, Field, computed_field
from pydantic.alias_generators import to_camel


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True


user = User(id=1, email="user-email", name="user-name")
print(f"{user=}")
print()

# lax-mode str(id) -> int(id)
external_data = {"id": "1", "email": "user-email", "name": "user-name", "is_active": False}
user_from_ext_data = User(**external_data)  # type: ignore
print(f"{user_from_ext_data=}")
print()

json_str = '{"id": "1", "email": "user-email", "name": "user-name", "is_active": false}'
user_from_json = User.model_validate_json(json_str)
print(f"{user_from_json=}")
print()


class TypedUser(TypedDict):
    id: int
    name: str
    email: str
    is_active: bool


typed_dict_user = User(**TypedUser(id=1, name="name-user", email="email-user", is_active=False))
print(f"{typed_dict_user=}")
print()


class Address(BaseModel):
    city: str
    zip_code: str


class User2(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True


user2 = User2(
    id=1, email="user-email", name="user-name", address=Address(city="City", zip_code="1234556")
)
print(f"{user2=}")
print()

user2_2 = User2(
    id=1,
    email="user-email",
    name="user-name",
    address={"city": "City", "zip_code": "1234556"},  # type: ignore
)
print(f"{user2_2=}")
print()

print(f"{user2.model_dump()=}")
print()
print(f"{user2.model_dump_json()=}")
print()


class User3(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive", default=True)


user3 = User3(id=1, name="user3-name", email="user3-email", isActive=False)
print(f"{user3=}")
print(f"{user3.model_dump()=}")
print(f"{user3.model_dump_json(by_alias=True)=}")
print()


class User4(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: int
    name: str
    email: str
    is_active: bool = True


user4 = User4(id=1, name="user4-name", email="user4-email", isActive=False)  # type: ignore
print(f"{user4=}")
print(f"{user4.model_dump()=}")
print(f"{user4.model_dump_json(by_alias=True)=}")
print()


class User5(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    is_active: bool = True

    @computed_field
    def greting(self) -> str:
        return f"Здравствуйте, {self.name}!"

    def get_user_info(self) -> str:
        return f"Name: {self.name}, email: {self.email}"


user5 = User5(name="user5-name", email="user5-email", is_active=False)
print(f"{user5=}")
print(f"{user5.get_user_info()=}")
print(f"{user5.greting=}")
print()
