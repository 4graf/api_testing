import allure
import pytest

from assertions.base_assertions import assert_http_status_code, assert_json_header
from assertions.calculator_assertions import assert_calculator_result, assert_calculator_not_int_error, \
    assert_calculator_params_count_error, \
    assert_calculator_oversize_error, assert_calculator_calculation_error
from data_providers.calculator_data_provider import CalculatorDataProvider
from models.calculator.numeric_operands import IntegerOperands, AnyOperands, OneOperand, ZeroOperands, ExtraOperands, \
    IncorrectNameOperands
from steps.calculator.calculator_schemas_steps import CalculatorSchemasSteps
from tests.utils import idfn


@allure.epic('Калькулятор')
@allure.feature('Вычисления калькулятора')
@allure.story('Целочисленное деление')
class TestDivision:

    @allure.title('Успешное деление двух целых чисел')
    @pytest.mark.parametrize("operands, expected_result",
                             CalculatorDataProvider.get_successful_division_data(),
                             ids=idfn)
    def test_successful_division_two_int_number(self, calculator_steps, operands: IntegerOperands, expected_result):
        response = calculator_steps.do_division(operands)

        assert_http_status_code(response=response, expected_code=200)
        assert_json_header(response=response)

        result = CalculatorSchemasSteps.get_calculation_result(response)
        assert_calculator_result(calculation_result=result, expected_result=expected_result)

    @allure.title('Безуспешное целочисленное деление на 0')
    @pytest.mark.parametrize("operands",
                             [IntegerOperands(x=5, y=0),
                              IntegerOperands(x=0, y=0)],
                             ids=idfn)
    def test_unsuccessful_remainder_by_zero(self, calculator_steps, operands):
        response = calculator_steps.do_division(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_calculation_error(calculation_error=error)

    @allure.title('Безуспешное деление с нецелочисленным числом')
    @pytest.mark.parametrize("operands",
                             CalculatorDataProvider.get_unsuccessful_not_int_data(),
                             ids=idfn)
    def test_unsuccessful_division_not_int_number(self, calculator_steps, operands: AnyOperands):
        response = calculator_steps.do_division(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_not_int_error(calculation_error=error)

    @allure.title('Безуспешное деление с числом, превышающим размер')
    @pytest.mark.parametrize("operands",
                             CalculatorDataProvider.get_unsuccessful_oversize_data(),
                             ids=idfn)
    def test_unsuccessful_division_oversize_number(self, calculator_steps, operands: AnyOperands):
        response = calculator_steps.do_division(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_oversize_error(calculation_error=error)

    @allure.title('Безуспешное деление с 1 параметром')
    def test_unsuccessful_division_with_one_number(self, calculator_steps):
        one_operand = OneOperand(x=5)

        response = calculator_steps.do_division(one_operand)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_params_count_error(calculation_error=error)

    @allure.title('Безуспешное деление без параметров')
    def test_unsuccessful_division_with_zero_numbers(self, calculator_steps):
        zero_operands = ZeroOperands()

        response = calculator_steps.do_division(zero_operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_params_count_error(calculation_error=error)

    @allure.title('Безуспешное деление с лишними параметрами')
    def test_unsuccessful_division_with_extra_numbers(self, calculator_steps):
        extra_operands = ExtraOperands(x=5, y=2, z=1)

        response = calculator_steps.do_division(extra_operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_params_count_error(calculation_error=error)

    @allure.title('Безуспешное деление с некорректными именами параметров')
    def test_unsuccessful_division_with_incorrect_name_numbers(self, calculator_steps):
        extra_operands = IncorrectNameOperands(x_value=5, y_value=2)

        response = calculator_steps.do_division(extra_operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_params_count_error(calculation_error=error)
