from typing import Any
from uuid import UUID

import allure
from jsonschema import Draft202012Validator, validate

# _checker =


@Draft202012Validator.FORMAT_CHECKER.checks(format="uuid4", raises=(ValueError, AttributeError))
def is_uuid4(instance):
    if not isinstance(instance, str):
        return True
    try:
        UUID(instance, version=4)
        return True
    except ValueError, AttributeError:
        return False


@allure.step("Validate json schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверить JSON-объект instance на соответствие json-схеме schema

    Args:
        instance (Any): JSON-объект
        schema (dict): json-схема

    Raises:
        jsonschema.exceptions.ValidationError: если объект не соответствует схеме
    """

    validate(instance=instance, schema=schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
