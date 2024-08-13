import allure
import pytest

from assertions.base_assertions import assert_http_status_code, assert_json_header
from assertions.calculator_assertions import assert_calculator_result, assert_calculator_not_int_error, \
    assert_calculator_params_count_error, \
    assert_calculator_oversize_error
from data_providers.calculator_data_provider import CalculatorDataProvider
from models.calculator.numeric_operands import IntegerOperands, AnyOperands, OneOperand, ZeroOperands, ExtraOperands, \
    IncorrectNameOperands
from steps.calculator_api.calculator_schemas_steps import CalculatorSchemasSteps
from steps.server_api.server_schemas_steps import ServerSchemasSteps
from tests.utils import idfn


@allure.epic('Калькулятор')
@allure.feature('Вычисления калькулятора')
@allure.story('Умножение')
class TestMultiplication:

    @allure.title('Успешное умножение двух целых чисел')
    @pytest.mark.parametrize("operands, expected_result",
                             CalculatorDataProvider.get_successful_multiplication_data(),
                             ids=idfn)
    def test_successful_multiplication_two_int_number(self, calculator_steps, operands: IntegerOperands, expected_result):
        response = calculator_steps.do_multiplication(operands)

        assert_http_status_code(response=response, expected_code=200)
        assert_json_header(response=response)

        result = CalculatorSchemasSteps.get_calculation_result(response)
        assert_calculator_result(calculation_result=result, expected_result=expected_result)

    @allure.title('Безуспешное умножение с нецелочисленным числом')
    @pytest.mark.parametrize("operands",
                             CalculatorDataProvider.get_unsuccessful_not_int_data(),
                             ids=idfn)
    def test_unsuccessful_multiplication_not_int_number(self, calculator_steps, operands: AnyOperands):
        response = calculator_steps.do_multiplication(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = ServerSchemasSteps.get_server_error(response)
        assert_calculator_not_int_error(calculation_error=error)

    @allure.title('Безуспешное умножение с числом, превышающим размер')
    @pytest.mark.parametrize("operands",
                             CalculatorDataProvider.get_unsuccessful_oversize_data(),
                             ids=idfn)
    def test_unsuccessful_multiplication_oversize_number(self, calculator_steps, operands: AnyOperands):
        response = calculator_steps.do_multiplication(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = ServerSchemasSteps.get_server_error(response)
        assert_calculator_oversize_error(calculation_error=error)

    @allure.title('Безуспешное умножение с 1 параметром')
    def test_unsuccessful_multiplication_with_one_number(self, calculator_steps):
        one_operand = OneOperand(x=5)

        response = calculator_steps.do_multiplication(one_operand)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = ServerSchemasSteps.get_server_error(response)
        assert_calculator_params_count_error(calculation_error=error)

    @allure.title('Безуспешное умножение без параметров')
    def test_unsuccessful_multiplication_with_zero_numbers(self, calculator_steps):
        zero_operands = ZeroOperands()

        response = calculator_steps.do_multiplication(zero_operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = ServerSchemasSteps.get_server_error(response)
        assert_calculator_params_count_error(calculation_error=error)

    @allure.title('Безуспешное умножение с лишними параметрами')
    def test_unsuccessful_multiplication_with_extra_numbers(self, calculator_steps):
        extra_operands = ExtraOperands(x=5, y=2, z=1)

        response = calculator_steps.do_multiplication(extra_operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = ServerSchemasSteps.get_server_error(response)
        assert_calculator_params_count_error(calculation_error=error)

    @allure.title('Безуспешное умножение с некорректными именами параметров')
    def test_unsuccessful_multiplication_with_incorrect_name_numbers(self, calculator_steps):
        extra_operands = IncorrectNameOperands(x_value=5, y_value=2)

        response = calculator_steps.do_multiplication(extra_operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = ServerSchemasSteps.get_server_error(response)
        assert_calculator_params_count_error(calculation_error=error)
