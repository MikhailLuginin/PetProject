import allure

from configs.config import base_settings
from pages.inputs_page.inputs_page import InputsPage
from tools.assertions.ui_assertions.base import BaseAssertions
from pages.inputs_page.inputs_locators import *
from tools.fakers import fakers
from tools.routes import APIRoutes


@allure.parent_suite('UI tests')
@allure.epic('UI tests')
@allure.feature('Тесты на ввод данных')
class TestInputs:

    @allure.title('Проверка ввода числа')
    def test_input_integer(self, clear_context_before_test, page):
        inputs_page = InputsPage(page)
        assertions = BaseAssertions(page)
        integer = fakers.random_integer()
        with allure.step("Переход на страницу авторизации"):
            inputs_page.open(f"{base_settings.base_url}{APIRoutes.inputs}")
        with allure.step("Ввод числа"):
            inputs_page.input_integer(value=integer)
        with allure.step("Нажатие кнопки Отображение входных данных"):
            inputs_page.click_button_visible_data()
        with allure.step("Проверка веденного числа"):
            assertions.have_text(output_integer_loc, integer)
