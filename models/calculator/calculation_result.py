"""
Модель ответа на запрос с арифметическим выражением.
"""

from pydantic import BaseModel, Field


class CalculationResult(BaseModel):
    """
    Ответ на запрос с арифметическим выражением.

    :ivar status_code: Код статуса ответа.
    :ivar result: Результат вычисления.
    """

    status_code: int = Field(alias='statusCode')
    result: int
