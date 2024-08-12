"""
Класс с эндпоинтами API калькулятора.
"""

import allure
from httpx import Response

from api.client.api_client import ApiClient
from models.calculator.numeric_operands import NumericOperands


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

        return self.api_client.get('/state')

    @allure.step(f'Сложение x и y')
    def addition(self, operands: NumericOperands) -> Response:
        """
        Эндпоинт сложения операндов.

        :param operands: Операнды x и y.
        :return: Ответ на запрос.
        """

        return self.api_client.post('/addition', json=operands.model_dump())

    @allure.step(f'Умножение x и y')
    def multiplication(self, operands: NumericOperands) -> Response:
        """
        Эндпоинт умножения операндов.

        :param operands: Операнды x и y.
        :return: Ответ на запрос.
        """

        return self.api_client.post('/multiplication', json=operands.model_dump())

    @allure.step(f'Целочисленное деление x на y')
    def division(self, operands: NumericOperands) -> Response:
        """
        Эндпоинт целочисленного деления операндов.

        :param operands: Операнды x и y.
        :return: Ответ на запрос.
        """

        return self.api_client.post('/division', json=operands.model_dump())

    @allure.step(f'Остаток от деления x на y')
    def remainder(self, operands: NumericOperands) -> Response:
        """
        Эндпоинт получения остатка от деления операндов.

        :param operands: Операнды x и y.
        :return: Ответ на запрос.
        """

        return self.api_client.post('/remainder', json=operands.model_dump())
