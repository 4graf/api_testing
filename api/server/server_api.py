"""
Класс с эндпоинтами API сервера.
"""

import allure
from httpx import Response

from api.client.api_client import ApiClient
from settings import ServerRoutesSettings

server_routes_settings = ServerRoutesSettings()


class ServerApi:
    """
    API сервера.

    :ivar api_client: HTTP клиент API.
    """

    def __init__(self, api_client: ApiClient):
        """
        Конструктор ServerApi.

        :param api_client: HTTP клиент API.
        """

        self.api_client = api_client

    @allure.step(f'Проверка состояния сервера')
    def state(self) -> Response:
        """
        Эндпоинт проверки состояния сервера.

        :return: Ответ на запрос.
        """

        return self.api_client.get(server_routes_settings.state)
