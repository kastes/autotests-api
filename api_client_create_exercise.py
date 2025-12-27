"""
Практикуемся в использовании API-клиентов.

1. Создать пользователя через API
2. Загрузить файл-превью курса
3. Создать курс
4. Создать упражнение
"""

from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    GetExercisesQuerySchema,
)
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema

# 1 Создать пользователя через API
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()
create_user_data = public_users_client.create_user(create_user_request)
print("User data: ", create_user_data)
print()

# Данные пользователя для авторизации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email, password=create_user_request.password
)

# 2 Загрузить файл-превью курса
files_client = get_files_client(authentication_user)
create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/pytest-logo.png")
create_file_data = files_client.create_file(create_file_request)
print("File data: ", create_file_data)
print()

# 3 Создать курс
courses_client = get_courses_client(authentication_user)
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_data.file.id,  # mypy упорно требует алиас :(
    createdByUserId=create_user_data.user.id,  # mypy упорно требует алиас :(
)
create_course_data = courses_client.create_course(create_course_request)
print("Course data: ", create_course_data)
print()

# 4 Создать упражнение (2 штуки)
exercises_client = get_exercises_client(authentication_user)
create_exercise_request = CreateExerciseRequestSchema(
    courseId=create_course_data.course.id, estimatedTime=None
)
create_exercise_data = exercises_client.create_exercise(create_exercise_request)
print("Exercise data: ", create_exercise_data)
print()

create_exercise_request = CreateExerciseRequestSchema(
    course_id=create_course_data.course.id  # type: ignore # mypy упорно требует алиас :(
)
create_exercise_data = exercises_client.create_exercise(create_exercise_request)
print("Exercise data: ", create_exercise_data)
print()

# 5 Получить список всех упражнений курса
get_exercises_query = GetExercisesQuerySchema(course_id=create_course_data.course.id)
get_exercises_data = exercises_client.get_exercises(get_exercises_query)
print("List exercises: ", get_exercises_data)
print()
