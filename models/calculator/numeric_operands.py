"""
Модель с числовыми операндами.
"""
from typing import Any

from pydantic import BaseModel, Field, field_validator


class BaseOperands(BaseModel):
    """
    Базовый класс для операндов
    """


class IntegerOperands(BaseOperands):
    """
    Целочисленные операнды.

    :ivar x: Левый операнд x.
    :ivar y: Правый операнд y.
    """

    x: int
    y: int


class AnyOperands(BaseOperands):
    """
    Операнды любого типа.

    :ivar x: Левый операнд x.
    :ivar y: Правый операнд y.
    """

    x: int | float | str | None = Field(union_mode='left_to_right', default=None)
    y: int | float | str | None = Field(union_mode='left_to_right', default=None)

    @field_validator('x', 'y', mode='after')
    @classmethod
    def empty_string_validator(cls, v: Any) -> int | float | str | None:
        if v == '':
            return None
        return v


class OneOperand(BaseOperands):
    """
    Операнд с одним числом.

    :ivar x: Левый операнд x.
    """

    x: int


class ZeroOperands(BaseOperands):
    """
    Ноль операндов.
    """


class IncorrectNameOperands(BaseOperands):
    """
    Операнды с некорректными именами.

    :ivar x_value: Левый операнд x_value.
    :ivar y_value: Правый операнд y_value.
    """

    x_value: int
    y_value: int


class ExtraOperands(BaseOperands):
    """
    Дополнительные операнды.

    :ivar x: Левый операнд x.
    :ivar y: Правый операнд y.
    :ivar z: Дополнительный операнд y.
    """

    x: int
    y: int
    z: int
