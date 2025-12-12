from typing import List, TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetExercisesQueryDict(TypedDict):
    """
    Описание GET-параметров запроса получить список упражнений курса с идентификатором courseId
    """

    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса создать упражнение
    """

    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class UpdateExerciseRequestDict(TypedDict, total=False):
    """
    Описание структуры запроса обновить упражнение
    """

    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class Exercise(TypedDict):
    """
    Описание структуры упражения
    """

    id: str
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос получить упражнение
    """

    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос получить список упражнениий
    """

    exercises: List[Exercise]


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос создать упражнение
    """

    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос обновить упражнение
    """

    exercise: Exercise


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

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получить список упражнений курса и вернуть данные в формате GetExercisesResponseDict

        :param query: GET-парметры с идентификатором курса
        :type query: GetExercisesQueryDict
        :return: Список упражнений курса в формате GetExercisesResponseDict
        :rtype: GetExercisesResponseDict
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получить упражнение по идентификатору

        :param exercise_id: Идентификатор упражнения
        :type exercise_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Получить упражнение по идентификатору и вернуть данные в формате GetExerciseResponseDict

        :param exercise_id: Идентификатор упражнения
        :type exercise_id: str
        :return: Данные упражнения в формате GetExerciseResponseDict
        :rtype: GetExerciseResponseDict
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создать упражнение

        :param request: Данные для создания упражнения
        :type request: CreateExerciseRequestDict
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Создать упражнение и вернуть данныe в формате CreateExerciseResponseDict

        :param request: Данные для создания упражнения
        :type request: CreateExerciseRequestDict
        :return: Данныe упражнения в формате CreateExerciseResponseDict
        :rtype: CreateExerciseResponseDict
        """
        response = self.create_exercise_api(request)
        return response.json()

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

    def update_exercise(
        self, exercise_id: str, request: UpdateExerciseRequestDict
    ) -> UpdateExerciseResponseDict:
        """
        Обновить упражнение и вернуть данные в формате UpdateExerciseResponseDict

        :param exercise_id: Идентификатор упражнения
        :type exercise_id: str
        :param request: Данные для обновленя упражнения
        :type request: UpdateExerciseRequestDict
        :return: Данные упражнения в формате UpdateExerciseResponseDict
        :rtype: UpdateExerciseResponseDict
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удалить упражнение

        :param exercise_id: Идентификатор упраженения
        :type exercise_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Создать экземпляр ExercisesClient для доступа к закрытой части API Execises
      для пользователя user

    :param user: Данные пользователя для аутентификации
    :type user: AuthenticationUserDict
    :return: Готовый к использованию экземпляр ExercisesClient
    :rtype: ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
