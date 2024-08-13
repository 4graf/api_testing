from models.calculator.calculation_error import CalculationError
from models.calculator.calculation_result import CalculationResult
from models.server_state import ServerState


def assert_server_state(server_state: ServerState):
    """
    Проверяет состояние сервера.

    :param server_state: Состояние сервера.
    """

    assert server_state.status_code == 0
    assert server_state.state == 'OK'


def assert_calculator_result(calculation_result: CalculationResult, expected_result: int):
    """
    Проверяет ответ калькулятора с ожидаемым значением.

    :param calculation_result: Ответ калькулятора.
    :param expected_result: Ожидаемый ответ.
    """

    assert calculation_result.status_code == 0
    assert calculation_result.result == expected_result


def assert_calculator_not_int_error(calculation_error: CalculationError):
    """
    Проверяет ошибку нецелочисленного вычисления калькулятора.

    :param calculation_error: Ошибка калькулятора.
    """

    assert calculation_error.status_code == 3
    assert calculation_error.status_message == 'Значения параметров должны быть целыми'


def assert_calculator_params_count_error(calculation_error: CalculationError):
    """
    Проверяет ошибку с недостаточным количеством чисел для вычисления калькулятором.

    :param calculation_error: Ошибка калькулятора.
    """

    assert calculation_error.status_code == 2
    assert calculation_error.status_message == 'Не указаны необходимые параметры'


def assert_calculator_calculation_error(calculation_error: CalculationError):
    """
    Проверяет ошибку вычисления.

    :param calculation_error: Ошибка калькулятора.
    """

    assert calculation_error.status_code == 1
    assert calculation_error.status_message == 'Ошибка вычисления'


def assert_calculator_incorrect_request_error(calculation_error: CalculationError):
    """
    Проверяет ошибку с неправильным форматом тела запроса.

    :param calculation_error: Ошибка калькулятора.
    """

    assert calculation_error.status_code == 5
    assert calculation_error.status_message == 'Неправильный формат тела запроса'
