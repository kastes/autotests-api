from typing import Any

from jsonschema import Draft202012Validator, validate


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверить JSON-объект instance на соответствие json-схеме schema

    Args:
        instance (Any): JSON-объект
        schema (dict): json-схема

    Raises:
        jsonschema.exceptions.ValidationError: если объект не соответствует схеме
    """
    # format_checker=Draft202012Validator.FORMAT_CHECKER - для проверки спец форматов (email, ...)
    validate(instance=instance, schema=schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
