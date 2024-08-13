"""
Логические шаги сценариев использования калькулятора.
"""
import allure
from httpx import Response

from api.calculator.calculator_api import CalculatorApi
from api.client.api_client import ApiClient
from models.calculator.numeric_operands import BaseOperands


# В рамках текущего проекта просто дублирует методы CalculatorApi
class CalculatorSteps:
    """
    Логические шаги сценариев использования калькулятора.

    :ivar calculator_api: API калькулятора.
    """

    def __init__(self, api_client: ApiClient):
        """
        Конструктор CalculatorSteps.

        :param api_client: API клиент.
        """

        self.calculator_api = CalculatorApi(api_client)

    @allure.step('Выполнить сложение чисел')
    def do_addition(self, operands: BaseOperands) -> Response:
        """
        Произвести сложение операндов.

        :param operands: Операнды x и y.
        :return: Ответ сервера на запрос.
        """

        return self.calculator_api.addition(operands.model_dump())

    @allure.step('Выполнить умножение чисел')
    def do_multiplication(self, operands: BaseOperands) -> Response:
        """
        Произвести умножение операндов.

        :param operands: Операнды x и y.
        :return: Ответ сервера на запрос.
        """

        return self.calculator_api.multiplication(operands.model_dump())

    @allure.step('Выполнить целочисленное деление чисел')
    def do_division(self, operands: BaseOperands) -> Response:
        """
        Произвести целочисленное деление операндов.

        :param operands: Операнды x и y.
        :return: Ответ сервера на запрос.
        """

        return self.calculator_api.division(operands.model_dump())

    @allure.step('Посчитать остаток от деления чисел')
    def do_remainder(self, operands: BaseOperands) -> Response:
        """
        Посчитать остаток от деления операндов.

        :param operands: Операнды x и y.
        :return: Ответ сервера на запрос.
        """

        return self.calculator_api.remainder(operands.model_dump())
