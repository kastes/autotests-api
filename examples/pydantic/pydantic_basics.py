"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""

import uuid

from pydantic import (
    UUID4,
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    HttpUrl,
    ValidationError,
)


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl = Field(frozen=True)


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID4 = Field(default_factory=uuid.uuid4)
    title: str
    max_score: int = Field(default=0, alias="maxScore")
    min_score: int = Field(default=0, alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(default="1 moment", alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


course = CourseSchema(
    title="Playwright",
    max_score=100,  # type: ignore
    minScore=10,
    description="Хороший курс!",
    preview_file=FileSchema(
        id="file-id",
        filename="file.png",
        directory="couses-preview",
        url=HttpUrl("http://localhos:8000/storage/"),
    ),
    # estimatedTime="1 day",
    createdByUser=UserSchema(
        id="user-id", email="user@mail.com", lastName="C", firstName="J", middleName="F"
    ),
)
print(f"{course=}")
print()

try:
    # попытка изменить frozen-поле!!
    course.preview_file.url = HttpUrl("http://localhost:8000/new_url")  # type: ignore
except ValidationError as e:
    print("Попытка записать в read only атрибут.")
    print(f"{e.errors()=}")
print()

user2 = UserSchema(
    id="user2-id", email="user2@mail.com", lastName="Doe", firstName="John", middleName="F"
)
print(f"{user2=}")
print()

course2 = CourseSchema(
    id=uuid.uuid4(),
    title="Playwright2",
    # - если убрать игнор типов с этого поля,
    # то все остальные поля дадут ошибку "неожиданный ключевой аргумент"
    max_score=100,  # type: ignore
    minScore=10,
    description="Хороший курс!",
    previewFile=FileSchema(
        id="file-id",
        filename="file.png",
        directory="couses-preview",
        url=HttpUrl("http://localhost:8000/storage/"),
    ),
    estimated_time="1 day",
    createdByUser=user2,
)
print(f"{course2=}")
print()


json_str = """
{
    "title":"Playwright",
    "max_score":100500,
    "minScore":50,
    "description":"Хороший курс!",
    "preview_file":{
        "id":"file-id",
        "filename":"file.png",
        "directory":"couses-preview",
        "url":"http://localhost:8000/storage/"
    },
    "createdByUser":{
        "id":"user-id",
        "email":"user@mail.com",
        "lastName":"JSON",
        "firstName":"J",
        "middleName":"F"
    }
}
"""
course_from_json = CourseSchema.model_validate_json(json_str)
print(f"{course_from_json=}")
print(f"{course_from_json.created_by_user.get_full_name()=}")
