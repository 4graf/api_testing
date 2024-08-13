"""
Логические шаги сценариев для работы с ответами сервера.
"""
from typing import Literal, Any

import allure
from httpx import Response

from api.client.api_client import ApiClient
from models.calculator.server_error import ServerError
from models.server_state import ServerState
from settings import CalculatorRoutesSettings

calculator_routes_settings = CalculatorRoutesSettings()


class ServerSchemasSteps:
    """
    Логические шаги сценариев для проверки схем ответов сервера.

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

    @classmethod
    @allure.step('Получить ошибку сервера из ответа')
    def get_server_error(cls, response: Response) -> ServerError:
        return ServerError.model_validate(response.json())

    @classmethod
    @allure.step('Получить данные с состоянием сервера из ответа')
    def get_server_state(cls, response: Response) -> ServerState:
        return ServerState.model_validate(response.json())

