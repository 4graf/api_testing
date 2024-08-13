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


class CalculatorRoutesSettings(BaseSettings):
    """
    Эндпоинты калькулятора.

    :ivar addition: Эндпоинт сложения.
    :ivar multiplication: Эндпоинт умножения.
    :ivar division: Эндпоинт целочисленного деления.
    :ivar remainder: Эндпоинт остатка от деления.
    """

    state: str
    addition: str
    multiplication: str
    division: str
    remainder: str


class ServerRoutesSettings(BaseSettings):
    """
    Эндпоинты сервера.

    :ivar state: Эндпоинт состояния сервера.
    """

    state: str
