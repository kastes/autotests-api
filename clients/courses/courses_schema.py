from typing import Annotated

from pydantic import UUID4, BaseModel, ConfigDict, Field, StringConstraints

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class GetCoursesQuerySchema(BaseModel):
    """
    Описание GET-параметров запроса 'список курсов пользователя с идентификатором user_id'
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    user_id: UUID4 = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса 'создать курс'
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=250)
    ] = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int | None = Field(default_factory=fake.min_score, alias="minScore")
    description: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)] = Field(
        default_factory=fake.text
    )
    estimated_time: Annotated[str, StringConstraints(min_length=1, max_length=50)] | None = Field(
        default_factory=fake.estimated_time, alias="estimatedTime"
    )
    preview_file_id: UUID4 = Field(default_factory=fake.uuid4, alias="previewFileId")
    created_by_user_id: UUID4 = Field(default_factory=fake.uuid4, alias="createdByUserId")


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса 'обновить курс'
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int | None = Field(default_factory=fake.min_score, alias="minScore")
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time, alias="estimatedTime")


class CourseSchema(BaseModel):
    """
    Описание структуры 'Course'
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: UUID4
    title: Annotated[str, StringConstraints(strip_whitespace=True, max_length=250)]
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: Annotated[str, StringConstraints(min_length=1, max_length=50)] | None = Field(
        alias="estimatedTime"
    )
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа 'создать курс'
    """

    course: CourseSchema


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа 'обновить курс'
    """

    course: CourseSchema
