from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ValidationErrorSchema(BaseModel):
    """
    Описание структуры ошибки валидации
    """

    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    type: str
    location: list[str | int] = Field(alias="loc")
    message: str = Field(alias="msg")
    input: Any
    context: dict[str, Any] = Field(alias="ctx")


class ValidationErrorResponseSchema(BaseModel):
    """
    Описание структуры ответа API с ошибками валидации
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    details: list[ValidationErrorSchema] = Field(alias="detail")


class InternalErrorResponseSchema(BaseModel):
    """
    Описание структуры ответа внутренней ошибки
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    details: str = Field(alias="detail")
