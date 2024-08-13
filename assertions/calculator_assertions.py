from assertions.base_assertions import assert_internal_status_code
from models.calculator.server_error import ServerError
from models.calculator.calculation_result import CalculationResult


def assert_calculator_result(calculation_result: CalculationResult, expected_result: int):
    """
    Проверяет ответ калькулятора с ожидаемым значением.

    :param calculation_result: Ответ калькулятора.
    :param expected_result: Ожидаемый ответ.
    """

    assert_internal_status_code(calculation_result, 0)
    assert calculation_result.result == expected_result, \
        f'expected result: {expected_result}\nactual result: {calculation_result.result}\n'


def assert_calculator_not_int_error(calculation_error: ServerError):
    """
    Проверяет ошибку нецелочисленного вычисления калькулятора.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 3)
    expected_message = 'Значения параметров должны быть целыми'
    assert calculation_error.status_message == expected_message, \
        (f'expected message: {expected_message}\n'
         f'actual message: {calculation_error.status_message}\n')


def assert_calculator_oversize_error(calculation_error: ServerError):
    """
    Проверяет ошибку превышения размера параметра для вычисления калькулятора.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 4)
    expected_message = 'Превышены максимальные значения параметров'
    assert calculation_error.status_message == expected_message, \
        (f'expected message: {expected_message}\n'
         f'actual message: {calculation_error.status_message}\n')


def assert_calculator_params_count_error(calculation_error: ServerError):
    """
    Проверяет ошибку с недостаточным количеством чисел для вычисления калькулятором.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 2)
    expected_message = 'Не указаны необходимые параметры'
    assert calculation_error.status_message == expected_message, \
        (f'expected message: {expected_message}\n'
         f'actual message: {calculation_error.status_message}\n')


def assert_calculator_calculation_error(calculation_error: ServerError):
    """
    Проверяет ошибку вычисления.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 1)
    expected_message = 'Ошибка вычисления'
    assert calculation_error.status_message == expected_message, \
        (f'expected message: {expected_message}\n'
         f'actual message: {calculation_error.status_message}\n')



def assert_calculator_incorrect_request_error(calculation_error: ServerError):
    """
    Проверяет ошибку с неправильным форматом тела запроса.

    :param calculation_error: Ошибка калькулятора.
    """

    assert_internal_status_code(calculation_error, 5)
    expected_message = 'Неправильный формат тела запроса'
    assert calculation_error.status_message == expected_message, \
        (f'expected message: {expected_message}\n'
         f'actual message: {calculation_error.status_message}\n')
