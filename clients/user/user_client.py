import allure
from httpx import Response

from clients.api_client import ApiClient
from schemas.user.user_schemas import CreateUserSchema, LoginUserSchema, UpdateUserSchema
from tools.routes import APIRoutes


class UserClient(ApiClient):

    @allure.step("Создание юзера")
    def create_user_api(self, body: CreateUserSchema) -> Response:
        return self.post(f"{APIRoutes.notes}{APIRoutes.API}{APIRoutes.user}{APIRoutes.register}",
                         json=body.model_dump(mode='json'))

    @allure.step("Авторизация юзера")
    def login_user_api(self, body: LoginUserSchema) -> Response:
        return self.post(f"{APIRoutes.notes}{APIRoutes.API}{APIRoutes.user}{APIRoutes.login}",
                         json=body.model_dump(mode='json'))

    @allure.step("Получение данных юзера")
    def get_user_api(self) -> Response:
        return self.get(f"{APIRoutes.notes}{APIRoutes.API}{APIRoutes.user}{APIRoutes.profile}")

    @allure.step("Изменение данных юзера")
    def update_user_api(self, body: UpdateUserSchema) -> Response:
        return self.patch(f"{APIRoutes.notes}{APIRoutes.API}{APIRoutes.user}{APIRoutes.profile}",
                          json=body.model_dump(mode='json'))
