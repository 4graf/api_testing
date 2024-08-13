"""
Модель ответа на запрос о состоянии сервера.
"""

from pydantic import BaseModel, Field


class ServerState(BaseModel):
    """
    Состояние сервера.

    :ivar status_code: Код статуса ответа.
    :ivar state: Состояние сервера.
    """

    status_code: int = Field(alias='statusCode')
    state: str
