from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import (
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    GetCoursesQuerySchema,
    GetCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.behaviors import AllureEpic, AllureFeature, AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.courses import (
    assert_create_course_response,
    assert_get_courses_response,
    assert_update_course_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
class TestCourses:
    @allure.title("Update course")
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
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

    @allure.title("Get courses")
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.severity(Severity.BLOCKER)
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

    @allure.title("Create course")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_course(
        self,
        courses_client: CoursesClient,
        function_file: FileFixture,
        function_user: UserFixture,
    ) -> None:
        """
        Тест сценария 'создать курс'
        """
        request = CreateCourseRequestSchema(
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id,
        )
        response = courses_client.create_course_api(request)

        response_data = CreateCourseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(response_data, request)
        validate_json_schema(response.json(), CreateCourseResponseSchema.model_json_schema())
        validate_json_schema(response.json(), CreateCourseResponseSchema.model_json_schema())
        validate_json_schema(response.json(), CreateCourseResponseSchema.model_json_schema())
