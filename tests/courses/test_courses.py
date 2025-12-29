from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import (
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response
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
