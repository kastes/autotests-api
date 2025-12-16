from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)


class ExercisesClient(APIClient):
    """
    Клиент API упражнений /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Получить список упражнений курса

        :param query: GET-парметры с идентификатором курса
        :type query: GetExercisesQuerySchema
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получить список упражнений курса и вернуть данные в формате GetExercisesResponseSchema

        :param query: GET-парметры с идентификатором курса
        :type query: GetExercisesQuerySchema
        :return: Список упражнений курса в формате GetExercisesResponseSchema
        :rtype: GetExercisesResponseSchema
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получить упражнение по идентификатору

        :param exercise_id: Идентификатор упражнения
        :type exercise_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Получить упражнение по идентификатору и вернуть данные в формате GetExerciseResponseSchema

        :param exercise_id: Идентификатор упражнения
        :type exercise_id: str
        :return: Данные упражнения в формате GetExerciseResponseSchema
        :rtype: GetExerciseResponseSchema
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создать упражнение

        :param request: Данные для создания упражнения
        :type request: CreateExerciseRequestSchema
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(mode="json", by_alias=True))

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создать упражнение и вернуть данныe в формате CreateExerciseResponseSchema

        :param request: Данные для создания упражнения
        :type request: CreateExerciseRequestSchema
        :return: Данныe упражнения в формате CreateExerciseResponseSchema
        :rtype: CreateExerciseResponseSchema
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Обновить упражнение

        :param exercise_id: Идентификатор упражнения
        :type exercise_id: str
        :param request: Данные для обновленя упражнения
        :type request: UpdateExerciseRequestSchema
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.patch(
            f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True)
        )

    def update_exercise(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> UpdateExerciseResponseSchema:
        """
        Обновить упражнение и вернуть данные в формате UpdateExerciseResponseSchema

        :param exercise_id: Идентификатор упражнения
        :type exercise_id: str
        :param request: Данные для обновленя упражнения
        :type request: UpdateExerciseRequestSchema
        :return: Данные упражнения в формате UpdateExerciseResponseSchema
        :rtype: UpdateExerciseResponseSchema
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удалить упражнение

        :param exercise_id: Идентификатор упраженения
        :type exercise_id: str
        :return: Ответ сервера
        :rtype: httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Создать экземпляр ExercisesClient для доступа к закрытой части API Execises
      для пользователя user

    :param user: Данные пользователя для аутентификации
    :type user: AuthenticationUserSchema
    :return: Готовый к использованию экземпляр ExercisesClient
    :rtype: ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
