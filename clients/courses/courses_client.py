import allure
from httpx import Response

from clients.api_client import APIClient
from clients.courses.courses_schema import (
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    GetCoursesQuerySchema,
    UpdateCourseRequestSchema,
)
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)


class CoursesClient(APIClient):
    """
    Клиент API курсов /api/v1/courses
    """

    @allure.step("Get list courses")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Получить список курсов пользователя

        :param query: GET-парметры с идентификатором пользователя
        :type query: GetCoursesQuerySchema
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    @allure.step("Get course by id {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Получить курс

        :param course_id: Идентификатор курса
        :type course_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    @allure.step("Create course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Создать курс

        :param request: Данные для создания курса
        :type request: CreateCourseRequestSchema
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(mode="json", by_alias=True))

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Создать курс и вернуть данные в формате CreateCourseResponseSchema

        :param request: Данные для создания курса
        :type request: CreateCourseRequestSchema
        :return: Данные курса
        :rtype: CreateCourseResponseSchema
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    @allure.step("Update course by id {course_id}")
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Обновить курс

        :param course_id: Идентификатор курса
        :type course_id: str
        :param request: Данные для обновленя курса
        :type request: UpdateCourseRequestSchema
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete course by id {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Удалить курс

        :param course_id: Идентификатор курса
        :type course_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Создать экземпляр CoursesClient с настройками доступа к закрытой части API
      для пользователя user.

    :param user: Данные пользователя для аутентификации
    :type user: AuthenticationUserSchema
    :return: Готовый к использованию экземпляр CoursesClient
    :rtype: CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user=user))
