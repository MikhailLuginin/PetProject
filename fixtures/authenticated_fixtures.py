from http import HTTPStatus
import pytest

from clients.builder import get_http_client
from clients.user.user_client import UserClient
from configs.config import DataUser
from schemas.user.user_schemas import LoginUserSchema, UserSchema
from tools.assertions.base import assert_status_code


@pytest.fixture(scope="function")
def authentications_client() -> UserClient:
    http_client = get_http_client()
    return UserClient(client=http_client)


@pytest.fixture(autouse=True, scope="function")
def auto_authorize(request, authentications_client: UserClient):
    # Если у теста стоит mark no_auto_auth, то фикстуру пропускаем
    if request.node.get_closest_marker("no_auto_authorize"):
        return
    """
    Авто-авторизация перед каждым тестом
    Берём логин/пароль из data_user.json
    Получаем токен и кладём в data_user.json
    """
    login_request = LoginUserSchema(
        email=DataUser.user_email(),
        password=DataUser.user_password()
    )
    login_response = authentications_client.login_user_api(body=login_request)

    assert_status_code(login_response.status_code, HTTPStatus.OK)

    login_schema = UserSchema.model_validate_json(login_response.text)
    token = login_schema.data.token
    DataUser.set_token(token)
