from http import HTTPStatus

import allure
import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
)
from fixtures.users import UserFixture
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import (
    assert_create_user_response,
    assert_get_user_response,
)
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
class TestUsers:
    @pytest.mark.parametrize("domain", ("mail.ru", "gmail.com", "example.com"))
    @allure.title("Create user")
    @allure.tag(AllureTag.CREATE_ENTITY)
    def test_create_user(self, domain: str, public_users_client: PublicUsersClient) -> None:
        """
        Тест сценария 'создать пользователя'
        """
        # Формируем тело запроса на создание пользователя
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        # Отправляем запрос на создание пользователя
        response = public_users_client.create_user_api(request)

        # Проверяем статус-код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Инициализируем модель ответа на основе полученного JSON в ответе
        # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся,
        # что ответ может быть преобразован в модель
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # Проверяем, что данные ответа совпадают с данными запроса
        assert_create_user_response(request, response_data)

        # проверим json-schema ответа API
        validate_json_schema(response.json(), CreateUserResponseSchema.model_json_schema())

    @allure.title("Get user me")
    @allure.tag(AllureTag.GET_ENTITY)
    def test_get_user_me(
        self, private_users_client: PrivateUsersClient, function_user: UserFixture
    ) -> None:
        """
        Тест сценария 'получить текущего пользователя'
        """
        response = private_users_client.get_user_me_api()

        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_get_user_response(
            create_user_response=function_user.response, get_user_response=response_data
        )

        validate_json_schema(response.json(), GetUserResponseSchema.model_json_schema())
