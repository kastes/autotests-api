from typing import Annotated

from pydantic import UUID4, BaseModel, ConfigDict, Field, StringConstraints

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


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

    title: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=250)]
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")
    description: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    estimated_time: Annotated[str, StringConstraints(min_length=1, max_length=50)] | None = Field(
        default=None, alias="estimatedTime"
    )
    preview_file_id: UUID4 = Field(alias="previewFileId")
    created_by_user_id: UUID4 = Field(alias="createdByUserId")


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса 'обновить курс'
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: (
        Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=250)]
        | None
    ) = Field(default=None)
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")
    description: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)] | None = (
        Field(default=None)
    )
    estimated_time: (
        Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)] | None
    ) = Field(default=None, alias="estimatedTime")


class CourseSchema(BaseModel):
    """
    Описание структуры 'Course'
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: UUID4
    title: Annotated[str, StringConstraints(strip_whitespace=True, max_length=250)]
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")
    description: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: Annotated[str, StringConstraints(min_length=1, max_length=50)] | None = Field(
        default=None, alias="estimatedTime"
    )
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа 'создать курс'
    """

    course: CourseSchema
