import allure

from clients.courses.courses_schema import (
    CourseSchema,
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    GetCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from tools.assertions.base import assert_equal, assert_is_true, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


@allure.step("Check update course response")
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


@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema) -> None:
    """
    Проверить что фактические данные курса соответствуют ожидаемым

    Args:
        actual (CourseSchema): фактические данные курса
        expected (CourseSchema): ожидаемые данные курса
    Raises:
        AssertionError: если фактические данные курса не соответствуют ожидаемым.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


@allure.step("Check get list courses response")
def assert_get_courses_response(
    actual: GetCoursesResponseSchema, expected: list[CreateCourseResponseSchema]
) -> None:
    """
    Проверить что данные ответа 'получить список курсов пользователя' соответствуют ожидаемым

    Args:
        actual (GetCoursesResponseSchema): данные ответа 'получить список курсов пользователя'
        expected (list[CreateCourseResponseSchema]): список данных ответа 'создать курс'
    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым.
    """
    assert_length(actual.courses, expected, "courses")

    for index, item in enumerate(expected):
        assert_course(actual.courses[index], item.course)


@allure.step("Check create course response")
def assert_create_course_response(
    actual: CreateCourseResponseSchema, expected: CreateCourseRequestSchema
) -> None:
    """
    Проверить что данные ответа 'создать курс' соответствуют ожидаемым

    Args:
        actual (CreateCourseResponseSchema): данные ответа 'создать курс'
        expected (CreateCourseRequestSchema): данные запроса 'создать курс'
    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым.
    """
    assert_is_true(actual.course.id, "id")
    assert_equal(actual.course.title, expected.title, "title")
    assert_equal(actual.course.max_score, expected.max_score, "max_score")
    assert_equal(actual.course.min_score, expected.min_score, "min_score")
    assert_equal(actual.course.description, expected.description, "description")
    assert_equal(actual.course.estimated_time, expected.estimated_time, "estimated_time")

    assert_equal(actual.course.preview_file.id, expected.preview_file_id, "preview_file_id")
    assert_equal(
        actual.course.created_by_user.id, expected.created_by_user_id, "created_by_user_id"
    )
