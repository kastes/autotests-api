from clients import BASE_URL
from clients.files.files_schema import (
    CreateFileRequestSchema,
    CreateFileResponseSchema,
    FileSchema,
    GetFileResponseSchema,
)
from tools.assertions.base import assert_equal, assert_is_true


def assert_create_file_response(
    actual: CreateFileResponseSchema, expected: CreateFileRequestSchema
):
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


def assert_file(actual: FileSchema, expected: FileSchema):
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


def assert_get_file_response(actual: GetFileResponseSchema, expected: CreateFileResponseSchema):
    """
    Проверить данные ответа 'получить файл' на соответствие ожидаемым.

    Args:
        actual (GetFileResponseSchema): данныет ответа 'получить файл'
        expected (CreateFileResponseSchema): данные ответа 'создать файл'

    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым.
    """
    assert_file(actual.file, expected.file)
