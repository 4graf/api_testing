import csv
import os

from models.calculator.numeric_operands import IntegerOperands, AnyOperands


class CalculatorDataProvider:

    @classmethod
    def get_successful_addition_data(cls, path: str | None = None) -> list[tuple[IntegerOperands, int]]:
        if not path:
            path = os.path.join(os.path.dirname(__file__), 'data/addition.csv')

        return cls._get_operands_with_result(path)

    @classmethod
    def get_successful_multiplication_data(cls, path: str | None = None) -> list[tuple[IntegerOperands, int]]:
        if not path:
            path = os.path.join(os.path.dirname(__file__), 'data/multiplication.csv')

        return cls._get_operands_with_result(path)

    @classmethod
    def get_successful_division_data(cls, path: str | None = None) -> list[tuple[IntegerOperands, int]]:
        if not path:
            path = os.path.join(os.path.dirname(__file__), 'data/division.csv')

        return cls._get_operands_with_result(path)

    @classmethod
    def get_successful_remainder_data(cls, path: str | None = None) -> list[tuple[IntegerOperands, int]]:
        if not path:
            path = os.path.join(os.path.dirname(__file__), 'data/remainder.csv')

        return cls._get_operands_with_result(path)

    @classmethod
    def get_unsuccessful_not_int_data(cls, path: str | None = None) -> list[AnyOperands]:
        if not path:
            path = os.path.join(os.path.dirname(__file__), 'data/not_int_addition.csv')
        with open(path, 'r') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            data = [AnyOperands(x=row['x'], y=row['y']) for row in reader]

        return data

    @classmethod
    def _get_operands_with_result(cls, path: str) -> list[tuple[IntegerOperands, int]]:
        with open(path, 'r') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            data = [(IntegerOperands(x=row['x'], y=row['y']), int(row['result'])) for row in reader]

        return data
