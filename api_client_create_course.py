"""
Практикуемся в использовании API-клиентов.

1. Создать пользователя через API
2. Загрузить файл превью курса
3. Создать курс
"""

from clients.courses.courses_client import CreateCourseRequestDict, get_courses_client
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

# 2 Загрузить файл превью курса
authentication_user = AuthenticationUserDict(
    email=create_user_request["email"], password=create_user_request["password"]
)
files_client = get_files_client(authentication_user)
create_file_request = CreateFileRequestDict(
    filename="python-logo.jpeg",
    directory="preview-courses",
    upload_file="./testdata/files/python-logo.jpeg",
)
create_file_data = files_client.create_file(create_file_request)
print("File data: ", create_file_data)
print()

# 3 Создать курс
courses_client = get_courses_client(authentication_user)
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=1000,
    minScore=0,
    description="Курс по языку программирования Python",
    estimatedTime="1 year",
    previewFileId=create_file_data["file"]["id"],
    createdByUserId=create_user_data["user"]["id"],
)
create_course_data = courses_client.create_course(create_course_request)
print("Course data: ", create_course_data)
