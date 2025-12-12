"""
Практикуемся в использовании API-клиентов.

1. Создать пользователя через API
2. Загрузить файл-превью курса
3. Создать курс
4. Создать упражнение
"""

from clients.courses.courses_client import CreateCourseRequestDict, get_courses_client
from clients.exercises.exercises_client import (
    CreateExerciseRequestDict,
    GetExercisesQueryDict,
    get_exercises_client,
)
from clients.files.files_client import CreateFileRequestDict, get_files_client
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import (
    CreateUserRequestDict,
    get_public_users_client,
)
from tools.fakers import get_random_email

# 1 Создать пользователя через API
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string",
)
create_user_data = public_users_client.create_user(create_user_request)
print("User data: ", create_user_data)
print()

# Данные пользователя для авторизации
authentication_user = AuthenticationUserDict(
    email=create_user_request["email"], password=create_user_request["password"]
)

# 2 Загрузить файл-превью курса
files_client = get_files_client(authentication_user)
create_file_request = CreateFileRequestDict(
    filename="pytest-logo.png",
    directory="preview-courses",
    upload_file="./testdata/files/pytest-logo.png",
)
create_file_data = files_client.create_file(create_file_request)
print("File data: ", create_file_data)
print()

# 3 Создать курс
courses_client = get_courses_client(authentication_user)
create_course_request = CreateCourseRequestDict(
    title="Pytest",
    maxScore=1000,
    minScore=0,
    description="Курс по фреймворку тестирования Pytest",
    estimatedTime=None,
    previewFileId=create_file_data["file"]["id"],
    createdByUserId=create_user_data["user"]["id"],
)
create_course_data = courses_client.create_course(create_course_request)
print("Course data: ", create_course_data)
print()

# 4 Создать упражнение (2 штуки)
exercises_client = get_exercises_client(authentication_user)
create_exercise_request = CreateExerciseRequestDict(
    title="Упражнение 1",
    courseId=create_course_data["course"]["id"],
    maxScore=1,
    minScore=0,
    orderIndex=0,
    description="Первое упражнение курса.",
    estimatedTime=None,
)
create_exercise_data = exercises_client.create_exercise(create_exercise_request)
print("Exercise data: ", create_exercise_data)
print()

create_exercise_request = CreateExerciseRequestDict(
    title="Упражнение 2",
    courseId=create_course_data["course"]["id"],
    maxScore=1,
    minScore=0,
    orderIndex=1,
    description="Второе упражнение курса.",
    estimatedTime="1 moment",
)
create_exercise_data = exercises_client.create_exercise(create_exercise_request)
print("Exercise data: ", create_exercise_data)
print()

# 5 Получить список всех упражнений курса
get_exercises_query = GetExercisesQueryDict(courseId=create_course_data["course"]["id"])
get_exercises_data = exercises_client.get_exercises(get_exercises_query)
print("List exercises: ", get_exercises_data)
print()
