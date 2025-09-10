import allure
from httpx import Response

from clients.api_client import ApiClient
from schemas.user.user_schemas import CreateUserSchema, LoginUserSchema
from tools.routes import APIRoutes


class UserClient(ApiClient):

    @allure.step("Создание юзера")
    def create_user_api(self, body: CreateUserSchema) -> Response:
        return self.post(f"{APIRoutes.API}{APIRoutes.USER}/register", json=body.model_dump(mode='json'))

    @allure.step("Авторизация юзера")
    def login_user_api(self, body: LoginUserSchema) -> Response:
        return self.post(f"{APIRoutes.API}{APIRoutes.USER}/login", json=body.model_dump(mode='json'))

    @allure.step("Авторизация юзера")
    def get_user_api(self) -> Response:
        return self.get(f"{APIRoutes.API}{APIRoutes.USER}/profile")

