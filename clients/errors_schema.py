from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ValidationErrorSchema(BaseModel):
    """
    Описание структуры ошибки валидации
    """

    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str | int] = Field(alias="loc")


class ValidationErrorResponseSchema(BaseModel):
    """
    Описание структуры ответа API с ошибками валидации
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    details: list[ValidationErrorSchema] = Field(alias="detail")
