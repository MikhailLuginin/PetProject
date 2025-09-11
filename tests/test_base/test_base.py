import allure
from fixtures.authenticated_fixtures import *
from schemas.user.user_schemas import *
from tools.assertions.base import assert_status_code
from tools.assertions.shema import validate_json_schema
from tools.assertions.user.user import assert_create_user, assert_login_user


@allure.parent_suite('API tests')
@allure.epic('Base test')
@allure.feature('Базовый тест на создание юзера')
@pytest.mark.no_auto_authorize
class TestBase:

    @allure.title('Создания юзера')
    def test_create_user(self, authentications_client):
        with allure.step("Создание пользователя"):
            request_user = CreateUserSchema()
            user = authentications_client.create_user_api(body=request_user)
            schema = UserSchema.model_validate_json(user.text)
            assert_status_code(user.status_code, HTTPStatus.CREATED)
            assert_create_user(schema, request_user)
            validate_json_schema(instance=user.json(), schema=schema.model_json_schema())
        with allure.step("Запись данных для авторизации созданным пользователем в файл"):
            data_user = {
                "user_id": schema.data.id,
                "name": schema.data.name,
                "email": schema.data.email,
                "password": request_user.password
            }
            DataUser.save(data_user)
        with allure.step("Авторизация пользователя"):
            request = LoginUserSchema(email=request_user.email, password=request_user.password)
            login = authentications_client.login_user_api(body=request)
            schema = UserSchema.model_validate_json(login.text)
            assert_status_code(login.status_code, HTTPStatus.OK)
            assert_login_user(schema, request)
            validate_json_schema(instance=login.json(), schema=schema.model_json_schema())

