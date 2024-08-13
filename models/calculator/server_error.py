"""
Модель ответа на запрос, содержащий ошибку.
"""

from pydantic import BaseModel, Field


class ServerError(BaseModel):
    """
    Ответ на запрос, содержащий ошибку.

    :ivar status_code: Код статуса ответа.
    :ivar status_message: Сообщение об ошибке.
    """

    status_code: int = Field(alias='statusCode')
    status_message: str = Field(alias='statusMessage')
