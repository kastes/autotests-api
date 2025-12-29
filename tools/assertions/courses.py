from clients.courses.courses_schema import (
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from tools.assertions.base import assert_equal


def assert_update_course_response(
    actual: UpdateCourseResponseSchema, expected: UpdateCourseRequestSchema
) -> None:
    """
    Проверить что данные ответа 'обновить курс' соответствуют ожидаемым

    Args:
        actual (UpdateCourseResponseSchema): данные ответа 'обновить курс'
        expected (UpdateCourseRequestSchema): данные запроса 'обновить курс'

    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым.
    """
    assert_equal(actual.course.title, expected.title, "title")
    assert_equal(actual.course.max_score, expected.max_score, "max_score")
    assert_equal(actual.course.min_score, expected.min_score, "min_score")
    assert_equal(actual.course.description, expected.description, "description")
    assert_equal(actual.course.estimated_time, expected.estimated_time, "estimated_time")
