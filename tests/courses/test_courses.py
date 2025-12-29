from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import (
    GetCoursesQuerySchema,
    GetCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import (
    assert_get_courses_response,
    assert_update_course_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(
        self, function_course: CourseFixture, courses_client: CoursesClient
    ) -> None:
        """
        Тест сценария 'обновить курс'
        """
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(
            str(function_course.response.course.id), request
        )

        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(response_data, request)
        validate_json_schema(response.json(), UpdateCourseResponseSchema.model_json_schema())

    def test_get_courses(
        self,
        courses_client: CoursesClient,
        function_course: CourseFixture,
        function_user: UserFixture,
    ) -> None:
        """
        Тест сценария 'получить список курсов пользователя'
        """
        query = GetCoursesQuerySchema(user_id=str(function_user.response.user.id))
        response = courses_client.get_courses_api(query)

        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])
        validate_json_schema(response.json(), GetCoursesResponseSchema.model_json_schema())
