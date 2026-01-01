from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    ExerciseSchema,
    GetExerciseResponseSchema,
    GetExercisesResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from tools.assertions.base import assert_equal, assert_is_true, assert_length
from tools.assertions.errors import assert_internal_error_response


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema) -> None:
    """
    Проверить данные 'упражнение' на равенство

    Args:
        actual (ExerciseSchema): фактические данные 'упражнение'
        expected (ExerciseSchema): ожидаемые данные 'упражнение'
    Raises:
        AssertionError: если фактические и ожидаемые данные не равны
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_create_exercise_response(
    actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema
) -> None:
    """
    Проверить что данные ответа 'создать упражнение' соответствуют ожидаемым

    Args:
        actual (CreateExerciseResponseSchema): данные ответа 'создать упражнение'
        expected (CreateExerciseRequestSchema): данные запроса 'создать упражнение'
    Raises:
        AssertionError: если данные не ответа не соответствуют ожидаемым
    """
    assert_is_true(actual.exercise.id, "id")
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(
    actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema
) -> None:
    """
    Проверить что данные ответа 'получить упражнение' соответствуют ожидаемым

    Args:
        actual (GetExerciseResponseSchema): данные ответа 'получить упражнение'
        expected (CreateExerciseResponseSchema): данные ответа 'создать упражнение'
    Raises:
        AssertionError: если данные не ответа не соответствуют ожидаемым
    """
    assert_exercise(actual.exercise, expected.exercise)


def assert_update_exercise_response(
    actual: UpdateExerciseResponseSchema, expected: UpdateExerciseRequestSchema
) -> None:
    """
    Проверить что данные ответа 'обновить упражнение' соответствуют ожидаемым

    Args:
        actual (UpdateExerciseResponseSchema): данные ответа 'обновить упражнение'
        expected (UpdateExerciseRequestSchema): данные запроса 'обновить упражнение'
    Raises:
        AssertionError: если данные не ответа не соответствуют ожидаемым
    """
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")


def assert_exercise_not_found_response(actual: InternalErrorResponseSchema) -> None:
    """
    Проверить данные ответа 'упражнение не найдено на сервере'

    Args:
        actual (InternalErrorResponseSchema): фактические данные ответа
    Raises:
        AssertionError: если данные ответа не соответствуют ожидаемым "Exercise not found"
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)


def assert_get_exercises_response(
    actual: GetExercisesResponseSchema, expected: list[CreateExerciseResponseSchema]
) -> None:
    """
    Проверить что данные ответа 'получить список упражнений' соответствуют ожидаемым

    Args:
        actual (GetExercisesResponseSchema): данные ответа 'получить список упражнений'
        expected (list[CreateExerciseResponseSchema]): список данных ответа 'создать упражнение'
    Raises:
        AssertionError: если данные не ответа не соответствуют ожидаемым
    """
    assert_length(actual.exercises, expected, "exercises")

    for index, item in enumerate(expected):
        assert_exercise(actual.exercises[index], item.exercise)
