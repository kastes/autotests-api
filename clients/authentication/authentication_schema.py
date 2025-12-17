from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr

from tools.fakers import fake


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса аутентификации.
    """

    email: EmailStr = Field(default_factory=fake.email)
    password: SecretStr = Field(default_factory=lambda: SecretStr(fake.password()))


class TokenSchema(BaseModel):
    """
    Описание структуры токена аутентификации.
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    token_type: str = Field(default="bearer", alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):  # Добавили структуру ответа аутентификации
    """
    Описание структуры ответа аутентификации.
    """

    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса 'обновить токен'.
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)
