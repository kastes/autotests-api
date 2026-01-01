from typing import Annotated, List

from pydantic import UUID4, BaseModel, ConfigDict, Field, StringConstraints

from tools.fakers import fake


class GetExercisesQuerySchema(BaseModel):
    """
    Описание GET-параметров запроса 'получить список упражнений курса с идентификатором courseId'
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    course_id: UUID4 = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса 'создать упражнение'
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=250)
    ] = Field(default_factory=fake.sentence)
    course_id: UUID4 = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int | None = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int | None = Field(default_factory=fake.min_score, alias="minScore")
    order_index: int = Field(default_factory=fake.integer, alias="orderIndex")
    description: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)] = Field(
        default_factory=fake.text
    )
    estimated_time: Annotated[str, StringConstraints(min_length=1, max_length=50)] | None = Field(
        default_factory=fake.estimated_time, alias="estimatedTime"
    )


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса 'обновить упражнение'
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: (
        Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=250)]
        | None
    ) = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int | None = Field(default_factory=fake.min_score, alias="minScore")
    order_index: int | None = Field(default_factory=fake.integer, alias="orderIndex")
    description: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)] | None = (
        Field(default_factory=fake.text)
    )
    estimated_time: Annotated[str, StringConstraints(min_length=1, max_length=50)] | None = Field(
        default_factory=fake.estimated_time, alias="estimatedTime"
    )


class ExerciseSchema(BaseModel):
    """
    Описание структуры Exercise
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: UUID4
    title: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=250)]
    course_id: UUID4 = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    estimated_time: Annotated[str, StringConstraints(min_length=1, max_length=50)] | None = Field(
        alias="estimatedTime"
    )


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа 'получить упражнение'
    """

    exercise: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа 'получить список упражнениий'
    """

    exercises: List[ExerciseSchema]


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа 'создать упражнение'
    """

    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа 'обновить упражнение'
    """

    exercise: ExerciseSchema
