"""
Функции для работы с HTTP клиентом.
Включает в себя создание HTTP клиента API.
"""

import allure

from api.client.api_client import ApiClient
from settings import ApiSettings

api_settings = ApiSettings()


@allure.title('Создание ApiClient с базовым url = "{base_url}"')
def get_api_client(base_url: str = api_settings.base_url) -> ApiClient:
    """
    Создаёт HTTP клиента для работы с API.

    :param base_url: Базовый url API.
    :return: Клиент API.
    """

    return ApiClient(base_url=base_url)
