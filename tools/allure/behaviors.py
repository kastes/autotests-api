from enum import StrEnum


class AllureEpic(StrEnum):
    LMS = "LMS service"
    STUDENT = "Student service"
    ADMINISTRATION = "Administration service"


class AllureFeature(StrEnum):
    USERS = "Users"
    FILES = "Files"
    COURSES = "Courses"
    EXERCISES = "Exercises"
    AUTHENTICATION = "Authentication"


class AllureStory(StrEnum):
    LOGIN = "Login"

    GET_ENTITY = "Get entity"
    GET_ENTITIES = "Get entities"
    CREATE_ENTITY = "Create entity"
    UPDATE_ENTITY = "Update entity"
    DELETE_ENTITY = "Delete entity"
    VALIDATE_ENTITY = "Validate entity"
