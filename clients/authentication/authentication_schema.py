from pydantic import BaseModel, EmailStr, Field, SecretStr


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
    Описание структуры запроса обновить токена.
    """

    refresh_token: str = Field(alias="refreshToken")
