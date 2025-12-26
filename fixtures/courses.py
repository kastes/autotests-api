import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import (
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
)
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    """
    Данные запроса и ответа сценария 'создать курс'.
    """

    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    """
    Фикстура создаёт клиента доступа к закрытой части API /api/v1/courses
    от имени пользователя созданного фикстурой function_user

    Args:
        function_user (UserFixture): фикстура создаёт нового пользователя

    Returns:
        CoursesClient: клиент доступа к закрытой части API /api/v1/courses
    """
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(
    courses_client: CoursesClient, function_user: UserFixture, function_file: FileFixture
) -> CourseFixture:
    """
    Фикстура создаёт новый курс.

    Args:
        function_user (UserFixture): фикстура создаёт пользователя
        function_file (FileFixture): фикстура создаёт файл
        courses_client (CoursesClient): фикстура создаёт клиента доступа к api/v1/courses

    Returns:
        CourseFixture: данные запроса и ответа сценария 'создать курс'.
    """
    request = CreateCourseRequestSchema(
        previewFileId=function_file.response.file.id,
        createdByUserId=function_user.response.user.id,
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
