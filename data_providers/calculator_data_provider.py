import csv
import os

from models.calculator.numeric_operands import NumericOperands


class CalculatorDataProvider:

    @classmethod
    def get_successful_addition_data(cls, path: str | None = None) -> list[tuple[NumericOperands, int]]:
        if not path:
            path = os.path.join(os.path.dirname(__file__), 'data/addition.csv')
        with open(path, 'r') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            data = [(NumericOperands(x=row['x'], y=row['y']), int(row['sum'])) for row in reader]
            return data
