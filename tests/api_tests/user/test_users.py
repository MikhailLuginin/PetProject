import allure

from fixtures.authenticated_fixtures import *
from schemas.user.user_schemas import *
from tools.assertions.api_assertions.base import assert_status_code
from tools.assertions.api_assertions.shema import validate_json_schema
from tools.assertions.api_assertions.user.user import assert_update_user


@allure.parent_suite('API tests')
@allure.epic('API tests')
@allure.feature('Тесты на юзера')
class TestUsers:

    @allure.title('Получение данных юзера')
    def test_get_user(self, authentications_client):
        user = authentications_client.get_user_api()
        schema = UserSchema.model_validate_json(user.text)
        assert_status_code(user.status_code, HTTPStatus.OK)
        validate_json_schema(instance=user.json(), schema=schema.model_json_schema())

    @allure.title('Изменение данных юзера')
    def test_update_user(self, authentications_client):
        update_request = UpdateUserSchema()
        user = authentications_client.update_user_api(body=update_request)
        schema = UserSchema.model_validate_json(user.text)
        assert_status_code(user.status_code, HTTPStatus.OK)
        assert_update_user(schema, update_request)
        validate_json_schema(instance=user.json(), schema=schema.model_json_schema())
