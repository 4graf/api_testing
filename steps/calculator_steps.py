"""
Логические шаги сценариев использования калькулятора.
"""
import allure
from httpx import Response

from api.calculator.calculator_api import CalculatorApi
from api.client.api_client import ApiClient
from models.calculator.calculation_error import CalculationError
from models.calculator.calculation_result import CalculationResult
from models.calculator.numeric_operands import BaseOperands
from models.server_state import ServerState


# В рамках текущего проекта просто дублирует методы CalculatorApi
class CalculatorSteps:
    """
    Логические шаги сценариев использования калькулятора.

    :ivar calculator_api: API калькулятора.
    """

    def __init__(self, api_client: ApiClient):
        """
        Конструктор CalculatorSteps.

        :param api_client: API калькулятора.
        """

        self.calculator_api = CalculatorApi(api_client)

    def do_server_state(self) -> Response:
        """
        Получить состояние сервера.

        :return: Ответ сервера на запрос.
        """

        return self.calculator_api.state()

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

    @classmethod
    @allure.step('Получить данные с состоянием сервера из ответа')
    def get_server_state(cls, response: Response) -> ServerState:
        return ServerState.model_validate(response.json())

    @classmethod
    @allure.step('Получить результат вычисления калькулятора из ответа')
    def get_calculation_result(cls, response: Response) -> CalculationResult:
        return CalculationResult.model_validate(response.json())

    @classmethod
    @allure.step('Получить ошибку вычисления калькулятора из ответа')
    def get_calculation_error(cls, response: Response) -> CalculationError:
        return CalculationError.model_validate(response.json())
