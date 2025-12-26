from typing import Dict, Set, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def request_with_secret_to_dict(request: T, *, secret_fields: Set[str]) -> Dict[str, str]:
    """
    Вернуть словарь содержащий поля Pydantic модели {поле: значение}.
    Поля содержащие секретные (SecretStr) значения обрабатываются отдельно.

    Args:
        request (T): Pydantic модель
        secret_fields (Set[str]): множество полей содержащих секретные значения

    Returns:
        Dict[str, str]: словарь содержащий поля Pydantic модели {поле: значение}.
    """
    request_dict = request.model_dump(by_alias=True, exclude=secret_fields)
    for field in secret_fields:
        value = getattr(request, field, None)
        if value and hasattr(value, "get_secret_value"):
            request_dict[field] = getattr(request, field).get_secret_value()
    return request_dict
