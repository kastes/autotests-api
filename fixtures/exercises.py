import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    """
    Данные запроса и ответа сценария 'создать упражнение'.
    """

    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    """
    Фикстура создаёт клиента доступа к закрытой части API /api/v1/exercises
    от имени пользователя созданного фикстурой function_user

    Args:
        function_user (UserFixture): фикстура создаёт нового пользователя

    Returns:
        ExercisesClient: клиент доступа к закрытой части API /api/v1/exercises
    """
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
    exercises_client: ExercisesClient, function_course: CourseFixture
) -> ExerciseFixture:
    """
    Фикстура создаёт новое упражнение.

    Args:
        exercises_client (ExercisesClient): фикстура создаёт клиент доступа к /api/v1/exercises
        function_course (CourseFixture): фикстура создаёт курс

    Returns:
        ExerciseFixture: данные запроса и ответа сценария 'создать упражнение'.
    """
    request = CreateExerciseRequestSchema(courseId=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
