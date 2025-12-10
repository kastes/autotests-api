from typing import NotRequired, TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание GET-параметров запроса списка упражнений курса с идентификатором courseId
    """

    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса создания упражнения
    """

    title: str
    courseId: str
    maxScore: NotRequired[int]
    minScore: NotRequired[int]
    orderIndex: int
    description: str
    estimatedTime: NotRequired[str]


class UpdateExerciseRequestDict(TypedDict, total=False):
    """
    Описание структуры запроса обновления упражнения
    """

    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент API упражнений /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получить список упражнений курса

        :param query: GET-парметры с идентификатором курса
        :type query: GetExercisesQueryDict
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)  # type: ignore

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получить упражнение

        :param exercise_id: Идентификатор упражнения
        :type exercise_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создать упражнение

        :param request: Данные для создания упражнения
        :type request: CreateExerciseRequestDict
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновить упражнение

        :param exercise_id: Идентификатор упражнения
        :type exercise_id: str
        :param request: Данные для обновленя упражнения
        :type request: UpdateExerciseRequestDict
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удалить упражнение

        :param exercise_id: Идентификатор упраженения
        :type exercise_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
