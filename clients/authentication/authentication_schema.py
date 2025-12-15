from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса аутентификации.
    """

    email: EmailStr
    password: SecretStr


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

    refresh_token: str = Field(alias="refreshToken")
