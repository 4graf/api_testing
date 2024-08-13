"""
Класс с эндпоинтами API калькулятора.
"""

import allure
from httpx import Response

from api.client.api_client import ApiClient
from settings import CalculatorRoutesSettings

calculator_routes_settings = CalculatorRoutesSettings()


class CalculatorApi:
    """
    API калькулятора.

    :ivar api_client: HTTP клиент API.
    """

    def __init__(self, api_client: ApiClient):
        """
        Конструктор CalculatorApi.

        :param api_client: HTTP клиент API.
        """

        self.api_client = api_client

    @allure.step(f'Проверка состояния сервера')
    def state(self) -> Response:
        """
        Эндпоинт проверки состояния сервера.

        :return: Ответ на запрос.
        """

        return self.api_client.get(calculator_routes_settings.state)

    @allure.step(f'Сложение x и y')
    def addition(self, operands_payload: dict) -> Response:
        """
        Эндпоинт сложения операндов.

        :param operands_payload: Операнды x и y.
        :return: Ответ на запрос.
        """

        return self.api_client.post(calculator_routes_settings.addition, json=operands_payload)

    @allure.step(f'Умножение x и y')
    def multiplication(self, operands_payload: dict) -> Response:
        """
        Эндпоинт умножения операндов.

        :param operands_payload: Операнды x и y.
        :return: Ответ на запрос.
        """

        return self.api_client.post(calculator_routes_settings.multiplication, json=operands_payload)

    @allure.step(f'Целочисленное деление x на y')
    def division(self, operands_payload: dict) -> Response:
        """
        Эндпоинт целочисленного деления операндов.

        :param operands_payload: Операнды x и y.
        :return: Ответ на запрос.
        """

        return self.api_client.post(calculator_routes_settings.division, json=operands_payload)

    @allure.step(f'Остаток от деления x на y')
    def remainder(self, operands_payload: dict) -> Response:
        """
        Эндпоинт получения остатка от деления операндов.

        :param operands_payload: Операнды x и y.
        :return: Ответ на запрос.
        """

        return self.api_client.post(calculator_routes_settings.remainder, json=operands_payload)
