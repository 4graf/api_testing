"""
Модель с числовыми операндами.
"""

from pydantic import BaseModel


class NumericOperands(BaseModel):
    """
    Числовые операнды.

    :ivar x: Левый операнд x.
    :ivar y: Правый операнд y.
    """

    x: int | float
    y: int | float
