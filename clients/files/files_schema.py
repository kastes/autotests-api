from typing import Annotated

from pydantic import UUID4, BaseModel, Field, HttpUrl, StringConstraints, UrlConstraints

from tools.fakers import fake


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса 'создать файл'
    upload_file - путь к файлу который надо загрузить на сервер.
    На сервере файл будет сохранён с именем filename в directory.
    """

    filename: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=255)
    ] = Field(default_factory=lambda: f"{fake.uuid4_str()}.png")
    directory: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=1024)
    ] = Field(default="preview-courses")
    upload_file: str


class FileSchema(BaseModel):
    """
    Описание структуры File
    """

    id: UUID4
    filename: Annotated[str, StringConstraints(max_length=250)]
    directory: Annotated[str, StringConstraints(max_length=250)]
    url: Annotated[HttpUrl, UrlConstraints(max_length=2083)] = Field(frozen=True)


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа 'создать файл'
    """

    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    Описание структуры ответа 'получить файл'
    """

    file: FileSchema
