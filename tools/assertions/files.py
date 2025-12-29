from clients import BASE_URL
from clients.errors_schema import (
    InternalErrorResponseSchema,
    ValidationErrorResponseSchema,
    ValidationErrorSchema,
)
from clients.files.files_schema import (
    CreateFileRequestSchema,
    CreateFileResponseSchema,
    FileSchema,
    GetFileResponseSchema,
)
from tools.assertions.base import assert_equal, assert_is_true
from tools.assertions.errors import (
    assert_internal_error_response,
    assert_validation_error_response,
)


def assert_create_file_response(
    actual: CreateFileResponseSchema, expected: CreateFileRequestSchema
) -> None:
    """
    Проверить данные ответа 'создать файл' на соответствие данным запроса 'создать файл'.

    Args:
        actual (CreateFileResponseSchema): данные ответа 'создать файл'
        expected (CreateFileRequestSchema): данные запроса 'создать файл'

    Raises:
        AssertionError: если данные ответа не соответствуют данным запроса
    """
    expected_url = f"{BASE_URL}/static/{expected.directory}/{expected.filename}"

    assert_equal(str(actual.file.url), expected_url, "file URL")
    assert_equal(actual.file.directory, expected.directory, "file directory")
    assert_equal(actual.file.filename, expected.filename, "file filename")
    assert_is_true(actual.file.id, "file id")


def assert_file(actual: FileSchema, expected: FileSchema) -> None:
    """
    Проверить равенство ожидаемых и действительных данных файла.

    Args:
        actual (FileSchema): действительные данные файла
        expected (FileSchema): ожидаемые данные файла

    Raises:
        AssertionError: если данные не равны
    """
    assert_equal(actual.url, expected.url, "file URL")
    assert_equal(actual.directory, expected.directory, "file directory")
    assert_equal(actual.filename, expected.filename, "file filename")
    assert_equal(actual.id, expected.id, "file id")


def assert_get_file_response(
    actual: GetFileResponseSchema, expected: CreateFileResponseSchema
) -> None:
    """
    Проверить данные ответа 'получить файл' на соответствие ожидаемым.

    Args:
        actual (GetFileResponseSchema): фактические данные ответа 'получить файл'
        expected (CreateFileResponseSchema): фактические данные ответа 'создать файл'

    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым.
    """
    assert_file(actual.file, expected.file)


def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema) -> None:
    """
    Проверить что ответ API на создание файла с пустым именем файла соответствует ожидаемой ошибке

    Args:
        actual (ValidationErrorResponseSchema): полученный ответ API

    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым.
    """
    expected_validation_error = ValidationErrorSchema(
        type="string_too_short",
        location=["body", "filename"],
        message="String should have at least 1 character",
        input="",
        context={"min_length": 1},
    )
    expected_response = ValidationErrorResponseSchema(details=[expected_validation_error])

    assert_validation_error_response(actual=actual, expected=expected_response)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema) -> None:
    """
    Проверить что ответ API на создание файла с пустым именем каталога
    соответствует ожидаемой ошибке

    Args:
        actual (ValidationErrorResponseSchema): полученный ответ API

    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым.
    """
    expected_validation_error = ValidationErrorSchema(
        type="string_too_short",
        location=["body", "directory"],
        message="String should have at least 1 character",
        input="",
        context={"min_length": 1},
    )
    expected_response = ValidationErrorResponseSchema(details=[expected_validation_error])

    assert_validation_error_response(actual=actual, expected=expected_response)


def assert_create_file_with_empty_directory_and_filename_response(
    actual: ValidationErrorResponseSchema,
) -> None:
    """
    Проверить что ответ API на создание файла с пустым именем каталога
    и пустым именем файла соответствует ожидаемой ошибке

    Args:
        actual (ValidationErrorResponseSchema): полученный ответ API

    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым.
    """
    expected_empty_filename_validation_error = ValidationErrorSchema(
        type="string_too_short",
        location=["body", "filename"],
        message="String should have at least 1 character",
        input="",
        context={"min_length": 1},
    )
    expected_empty_directory_validation_error = ValidationErrorSchema(
        type="string_too_short",
        location=["body", "directory"],
        message="String should have at least 1 character",
        input="",
        context={"min_length": 1},
    )
    expected_response = ValidationErrorResponseSchema(
        details=[
            expected_empty_filename_validation_error,
            expected_empty_directory_validation_error,
        ]
    )

    assert_validation_error_response(actual=actual, expected=expected_response)


def assert_file_not_found_response(actual: InternalErrorResponseSchema) -> None:
    """
    Проверить данные ответа 'файл не найден на сервере'

    Args:
        actual (InternalErrorResponseSchema): фактические данные ответа
    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым "File not found"
    """
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)


def assert_get_file_with_incorrect_file_id_response(
    actual: ValidationErrorResponseSchema,
) -> None:
    """
    Проверить что данные ответа API 'получить файл с incorrect-file-id'
    соответствуют ожидаемой ошибке

    Args:
        actual (ValidationErrorResponseSchema): полученный ответ API
    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым.
    """
    expected_error = ValidationErrorSchema(
        type="uuid_parsing",
        location=["path", "file_id"],
        message="Input should be a valid UUID, invalid character: expected an optional prefix "
        "of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
        input="incorrect-file-id",
        context={
            "error": "invalid character: expected an optional prefix of `urn:uuid:` followed "
            "by [0-9a-fA-F-], found `i` at 1"
        },
    )
    expected = ValidationErrorResponseSchema(details=[expected_error])
    assert_validation_error_response(actual, expected)
