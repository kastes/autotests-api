from typing import NotRequired, TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetCoursesQueryDict(TypedDict):
    """
    Описание GET-параметров запроса курсов пользователя с идентификатором userId
    """

    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса создания курса
    """

    title: str
    maxScore: NotRequired[int]
    minScore: NotRequired[int]
    description: str
    estimatedTime: NotRequired[str]
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict, total=False):
    """
    Описание структуры запроса обновления курса
    """

    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


class CoursesClient(APIClient):
    """
    Клиент API курсов /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Получить список курсов пользователя

        :param query: GET-парметры с идентификатором пользователя
        :type query: GetCoursesQueryDict
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get("/api/v1/courses", params=query)  # type: ignore

    def get_course_api(self, course_id: str) -> Response:
        """
        Получить курс

        :param course_id: Идентификатор курса
        :type course_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Создать курс

        :param request: Данные для создания курса
        :type request: CreateCourseRequestDict
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Обновить курс

        :param course_id: Идентификатор курса
        :type course_id: str
        :param request: Данные для обновленя курса
        :type request: UpdateCourseRequestDict
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Удалить курс

        :param course_id: Идентификатор курса
        :type course_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Создать экземпляр CoursesClient с настройками доступа к закрытой части API
      для пользователя user.

    :param user: Данные пользователя для аутентификации
    :type user: AuthenticationUserDict
    :return: Готовый к использованию экземпляр CoursesClient
    :rtype: CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user=user))
