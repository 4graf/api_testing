from assertions.base_assertions import assert_internal_status_code
from models.calculator.calculation_error import CalculationError
from models.calculator.calculation_result import CalculationResult


def assert_calculator_result(calculation_result: CalculationResult, expected_result: int):
    """
    Проверяет ответ калькулятора с ожидаемым значением.

    :param calculation_result: Ответ калькулятора.
    :param expected_result: Ожидаемый ответ.
    """

    assert_internal_status_code(calculation_result, 0)
    assert calculation_result.result == expected_result


def assert_calculator_not_int_error(calculation_error: CalculationError):
    """
    Проверяет ошибку нецелочисленного вычисления калькулятора.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 3)
    assert calculation_error.status_message == 'Значения параметров должны быть целыми'


def assert_calculator_oversize_error(calculation_error: CalculationError):
    """
    Проверяет ошибку превышения размера параметра для вычисления калькулятора.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 4)
    assert calculation_error.status_message == 'Превышены максимальные значения параметров'


def assert_calculator_params_count_error(calculation_error: CalculationError):
    """
    Проверяет ошибку с недостаточным количеством чисел для вычисления калькулятором.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 2)
    assert calculation_error.status_message == 'Не указаны необходимые параметры'


def assert_calculator_calculation_error(calculation_error: CalculationError):
    """
    Проверяет ошибку вычисления.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 1)
    assert calculation_error.status_message == 'Ошибка вычисления'


def assert_calculator_incorrect_request_error(calculation_error: CalculationError):
    """
    Проверяет ошибку с неправильным форматом тела запроса.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 5)
    assert calculation_error.status_message == 'Неправильный формат тела запроса'
