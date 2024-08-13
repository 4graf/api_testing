"""
Логические шаги сценариев работы с сервером.
"""
import allure
from httpx import Response

from api.client.api_client import ApiClient
from api.server.server_api import ServerApi
from models.server_state import ServerState


class ServerSteps:
    """
    Логические шаги сценариев работы с сервером.

    :ivar server_api: API сервера.
    """

    def __init__(self, api_client: ApiClient):
        """
        Конструктор CalculatorSteps.

        :param api_client: API клиент.
        """

        self.server_api = ServerApi(api_client)

    def do_server_state(self) -> Response:
        """
        Получить состояние сервера.

        :return: Ответ сервера на запрос.
        """

        return self.server_api.state()
