"""
HTTP клиент для работы с тестируемым API.
"""

import allure
from httpx import Client, Response
from httpx._types import URLTypes


class ApiClient(Client):
    """
    HTTP клиент для работы с тестируемым API.
    """

    @allure.step('Отправка "{method}" запроса на "{url}"')
    def request(self, method: str, url: URLTypes, **kwargs) -> Response:
        """
        Расширение логики метода httpx request с записью Allure метода запроса и его url.

        :param method: HTTP метод.
        :param url: URL запроса.
        :return: Ответ на запрос.
        """

        return super().request(method, url, **kwargs)
