"""
Логические шаги сценариев использования калькулятора.
"""
from typing import Literal, Any

import allure
from httpx import Response

from api.client.api_client import ApiClient
from models.calculator.calculation_error import CalculationError
from models.calculator.calculation_result import CalculationResult
from models.server_state import ServerState
from settings import CalculatorRoutesSettings

calculator_routes_settings = CalculatorRoutesSettings()


class CalculatorSchemasSteps:
    """
    Логические шаги сценариев для проверки схем ответов калькулятора.

    :ivar api_client: API клиент.
    """

    METHODS = Literal['get', 'post', 'options', 'delete']

    def __init__(self, api_client: ApiClient):
        """
        Конструктор CalculatorSchemasSteps.

        :param api_client: API клиент.
        """

        self.api_client = api_client
    
    def send_request_to_state(self, method: METHODS, payload: Any | None = None) -> Response:
        """
        Отправить запрос на эндпоинт состояния сервера.

        :param method: HTTP метод запроса.
        :param payload: Данные тела запроса.
        :return: Ответ сервера на запрос.
        """
        body = payload.model_dump() if payload else None
        return self.api_client.request(url=calculator_routes_settings.state, method=method, json=body)

    def send_request_to_addition(self, method: METHODS, payload: Any | None = None) -> Response:
        """
        Отправить запрос на эндпоинт сложения.

        :param method: HTTP метод запроса.
        :param payload: Данные тела запроса.
        :return: Ответ сервера на запрос.
        """
        body = payload.model_dump() if payload else None
        return self.api_client.request(url=calculator_routes_settings.addition, method=method, json=body)
    
    def send_request_to_multiplication(self, method: METHODS, payload: Any | None = None) -> Response:
        """
        Отправить запрос на эндпоинт умножения.

        :param method: HTTP метод запроса.
        :param payload: Данные тела запроса.
        :return: Ответ сервера на запрос.
        """
        body = payload.model_dump() if payload else None
        return self.api_client.request(url=calculator_routes_settings.multiplication, method=method, json=body)
    
    def send_request_to_division(self, method: METHODS, payload: Any | None = None) -> Response:
        """
        Отправить запрос на эндпоинт целочисленного деления.

        :param method: HTTP метод запроса.
        :param payload: Данные тела запроса.
        :return: Ответ сервера на запрос.
        """
        body = payload.model_dump() if payload else None
        return self.api_client.request(url=calculator_routes_settings.division, method=method, json=body)
    
    def send_request_to_remainder(self, method: METHODS, payload: Any | None = None) -> Response:
        """
        Отправить запрос на эндпоинт вычисления остатка от деления.

        :param method: HTTP метод запроса.
        :param payload: Данные тела запроса.
        :return: Ответ сервера на запрос.
        """
        body = payload.model_dump() if payload else None
        return self.api_client.request(url=calculator_routes_settings.remainder, method=method, json=body)

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
