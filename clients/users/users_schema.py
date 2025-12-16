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
    Описание структуры пользователя.
    """

    # `populated_by_name` not recommended and will be deprecated in v3
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

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
    Описание структуры запроса 'создать пользователя'.
    """

    # `populated_by_name` not recommended and will be deprecated in v3
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

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
    Описание структуры данных ответа 'создать пользователя'.
    """

    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры данных ответа 'получить пользователя'
    """

    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса 'обновить пользовтеля'
    """

    # `populated_by_name` not recommended and will be deprecated in v3
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    email: (
        Annotated[EmailStr, StringConstraints(strip_whitespace=True, min_length=1, max_length=250)]
        | None
    ) = Field(default=None)

    last_name: (
        Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)] | None
    ) = Field(default=None, alias="lastName")

    first_name: (
        Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)] | None
    ) = Field(default=None, alias="firstName")

    middle_name: (
        Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)] | None
    ) = Field(default=None, alias="middleName")


class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры данных ответа 'обновить пользователя'
    """

    user: UserSchema
