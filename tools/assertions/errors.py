from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema
from tools.assertions.base import assert_equal, assert_length


def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema) -> None:
    """
    Проверить объект ошибки валидации на совпадение с ожидаемым значением
    Args:
        actual (ValidationErrorSchema): фактическая ошибка
        expected (ValidationErrorSchema): ожидаемая ошибка
    Raises:
        AssertionError: если фактическая ошибка не соответствует ожидаемой
    """
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.location, expected.location, "location")
    assert_equal(actual.context, expected.context, "context")


def assert_validation_error_response(
    actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema
) -> None:
    """
    Проверить ответ API с ошибками валидации на соответствие ожидаемому
    Args:
        actual (ValidationErrorResponseSchema): фактический ответ API
        expected (ValidationErrorResponseSchema): ожидаемый ответ API
    Raises:
        AssertionError: если фактический ответ не соответствует ожидаемому
    """
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)
