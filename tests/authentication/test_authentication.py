from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
)
from fixtures.users import UserFixture
from tools.allure.behaviors import AllureEpic, AllureFeature, AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHENTICATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.title("Login with correct email and password")
    @allure.story(AllureStory.LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_login(self, authentication_client: AuthenticationClient, function_user: UserFixture):
        """
        Тест сценария 'успешная аутентификация пользователя'
        """
        # тестируем процесс аутентификации созданного пользователя
        request = LoginRequestSchema(
            email=function_user.request.email, password=function_user.request.password
        )
        response = authentication_client.login_api(request)

        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_login_response(response_data)

        validate_json_schema(response.json(), LoginResponseSchema.model_json_schema())
