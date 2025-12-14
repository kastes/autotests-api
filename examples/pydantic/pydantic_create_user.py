from typing import Annotated

from pydantic import (
    UUID4,
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    SecretStr,
    StringConstraints,
)


class UserSchema(BaseModel):
    """
    Описание структуры пользователя
    """

    model_config = ConfigDict(populate_by_name=True)

    id: UUID4

    email: Annotated[
        EmailStr, StringConstraints(strip_whitespace=True, min_length=1, max_length=250)
    ]

    last_name: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)
    ] = Field(alias="lastName")

    first_name: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)
    ] = Field(alias="firstName")

    middle_name: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)
    ] = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса создать пользователя
    """

    model_config = ConfigDict(populate_by_name=True)

    email: Annotated[
        EmailStr, StringConstraints(strip_whitespace=True, min_length=1, max_length=250)
    ]

    password: Annotated[SecretStr, StringConstraints(min_length=1, max_length=250)]

    last_name: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)
    ] = Field(alias="lastName")

    first_name: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)
    ] = Field(alias="firstName")

    middle_name: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)
    ] = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создать пользователя
    """

    user: UserSchema


if __name__ == "__main__":
    import uuid

    user = UserSchema(
        id=uuid.uuid4(), email="user@mail.com", lastName="Doe", firstName="John", middleName="F"
    )
    print(f"{user=}")
    print()

    create_user_request = CreateUserRequestSchema(
        password=SecretStr("secret"),
        email="user@mail.com",
        lastName="Doe",
        firstName="John",
        middleName="F",
    )
    print(f"{create_user_request=}")
    print()

    create_user_response = CreateUserResponseSchema(user=user)
    print(f"{create_user_response=}")
    print()
