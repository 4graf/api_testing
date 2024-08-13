"""
Настройки проекта.
"""

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class ApiSettings(BaseSettings):
    """
    Настройки для работы с тестируемым API.

    :ivar base_url: Базовый url API.
    """

    base_url: str
