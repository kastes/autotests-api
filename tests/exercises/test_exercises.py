from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.allure.behaviors import AllureEpic, AllureFeature, AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response,
    assert_exercise_not_found_response,
    assert_get_exercise_response,
    assert_get_exercises_response,
    assert_update_exercise_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.EXERCISES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.EXERCISES)
class TestExercises:
    @allure.title("Create exercise")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_exercise(
        self, exercises_client: ExercisesClient, function_course: CourseFixture
    ) -> None:
        """
        Тест сценария 'создать упражнение'
        """
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)

        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(response_data, request)
        validate_json_schema(response.json(), CreateExerciseResponseSchema.model_json_schema())

    @allure.title("Get exercise")
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_get_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ) -> None:
        """
        Тест сценария 'получить упражнение'
        """
        response = exercises_client.get_exercise_api(str(function_exercise.response.exercise.id))

        response_data = GetExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)
        validate_json_schema(response.json(), GetExerciseResponseSchema.model_json_schema())

    @allure.title("Update exercise")
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_update_exercise(
        self, function_exercise: ExerciseFixture, exercises_client: ExercisesClient
    ) -> None:
        """
        Тест сценария 'обновить упражнение'
        """
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(
            str(function_exercise.response.exercise.id), request
        )

        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(response_data, request)
        validate_json_schema(response.json(), UpdateExerciseResponseSchema.model_json_schema())

    @allure.title("Delete exercise")
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_delete_exercise(
        self, function_exercise: ExerciseFixture, exercises_client: ExercisesClient
    ) -> None:
        """
        Тест сценария 'удалить упражнение'
        """
        delete_response = exercises_client.delete_exercise_api(
            str(function_exercise.response.exercise.id)
        )

        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(
            str(function_exercise.response.exercise.id)
        )

        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), InternalErrorResponseSchema.model_json_schema())

    @allure.title("Get exercises")
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.severity(Severity.BLOCKER)
    def test_get_exercises(
        self,
        exercises_client: ExercisesClient,
        function_course: CourseFixture,
        function_exercise: ExerciseFixture,
    ) -> None:
        """
        Тест сценария 'получить список упражнений'
        """
        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query)

        response_data = GetExercisesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])
        validate_json_schema(response.json(), GetExercisesResponseSchema.model_json_schema())
