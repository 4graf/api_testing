import allure
import pytest

from assertions.base_assertions import assert_http_status_code, assert_json_header
from assertions.calculator_assertions import assert_calculator_result, assert_server_state, \
    assert_calculator_not_int_error, assert_calculator_params_count_error, assert_calculator_calculation_error
from data_providers.calculator_data_provider import CalculatorDataProvider
from models.calculator.numeric_operands import IntegerOperands, AnyOperands, OneOperand, ZeroOperands
from steps.calculator_schemas_steps import CalculatorSchemasSteps
from tests.utils import idfn


@allure.epic('Калькулятор')
@allure.feature('Вычисления калькулятора')
class TestCalculator:

    @allure.story('Состояние сервера')
    @allure.title('Состояние сервера - запущен')
    def test_server_state(self, calculator_steps):
        response = calculator_steps.do_server_state()
        assert_http_status_code(response=response, expected_code=200)
        assert_json_header(response=response)

        state = CalculatorSchemasSteps.get_server_state(response)
        assert_server_state(server_state=state)

    @allure.story('Сложение')
    @allure.title('Успешное сложение двух целых чисел')
    @pytest.mark.parametrize("operands, expected_result",
                             CalculatorDataProvider.get_successful_addition_data(),
                             ids=idfn)
    def test_successful_addition_two_int_number(self, calculator_steps, operands: IntegerOperands, expected_result):
        response = calculator_steps.do_addition(operands)

        assert_http_status_code(response=response, expected_code=200)
        assert_json_header(response=response)

        result = CalculatorSchemasSteps.get_calculation_result(response)
        assert_calculator_result(calculation_result=result, expected_result=expected_result)

    @allure.story('Умножение')
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

    @allure.story('Деление')
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

    @allure.story('Остаток от деления')
    @allure.title('Успешное вычисление остатка от деления двух целых чисел')
    @pytest.mark.parametrize("operands, expected_result",
                             CalculatorDataProvider.get_successful_remainder_data(),
                             ids=idfn)
    def test_successful_remainder_two_int_number(self, calculator_steps, operands: IntegerOperands, expected_result):
        response = calculator_steps.do_remainder(operands)

        assert_http_status_code(response=response, expected_code=200)
        assert_json_header(response=response)

        result = CalculatorSchemasSteps.get_calculation_result(response)
        assert_calculator_result(calculation_result=result, expected_result=expected_result)

    @allure.story('Сложение')
    @allure.title('Безуспешное сложение с нецелочисленным числом')
    @pytest.mark.parametrize("operands",
                             CalculatorDataProvider.get_unsuccessful_not_int_data(),
                             ids=idfn)
    def test_unsuccessful_addition_not_int_number(self, calculator_steps, operands: AnyOperands):
        response = calculator_steps.do_addition(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_not_int_error(calculation_error=error)

    @allure.story('Сложение')
    @allure.title('Безуспешное сложение с 1 параметром')
    def test_unsuccessful_addition_with_one_number(self, calculator_steps):
        one_operand = OneOperand(x=5)

        response = calculator_steps.do_addition(one_operand)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_params_count_error(calculation_error=error)

    @allure.story('Сложение')
    @allure.title('Безуспешное сложение без параметров')
    def test_unsuccessful_addition_with_zero_numbers(self, calculator_steps):
        zero_operands = ZeroOperands()

        response = calculator_steps.do_addition(zero_operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_params_count_error(calculation_error=error)

    @allure.story('Умножение')
    @allure.title('Безуспешное умножение с нецелочисленным числом')
    @pytest.mark.parametrize("operands",
                             CalculatorDataProvider.get_unsuccessful_not_int_data(),
                             ids=idfn)
    def test_unsuccessful_multiplication_not_int_number(self, calculator_steps, operands: AnyOperands):
        response = calculator_steps.do_multiplication(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_not_int_error(calculation_error=error)

    @allure.story('Целочисленное деление')
    @allure.title('Безуспешное целочисленное деление с нецелочисленным числом')
    @pytest.mark.parametrize("operands",
                             CalculatorDataProvider.get_unsuccessful_not_int_data(),
                             ids=idfn)
    def test_unsuccessful_division_not_int_number(self, calculator_steps, operands: AnyOperands):
        response = calculator_steps.do_division(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_not_int_error(calculation_error=error)

    @allure.story('Целочисленное деление')
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

    @allure.story('Остаток от деления')
    @allure.title('Безуспешное вычисление остатка от деления с нецелочисленным числом')
    @pytest.mark.parametrize("operands",
                             CalculatorDataProvider.get_unsuccessful_not_int_data(),
                             ids=idfn)
    def test_unsuccessful_remainder_not_int_number(self, calculator_steps, operands: AnyOperands):
        response = calculator_steps.do_remainder(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_not_int_error(calculation_error=error)

    @allure.story('Остаток от деления')
    @allure.title('Безуспешное вычисление остатка от деления на 0')
    @pytest.mark.parametrize("operands",
                             [IntegerOperands(x=5, y=0),
                              IntegerOperands(x=0, y=0)],
                             ids=idfn)
    def test_unsuccessful_division_by_zero(self, calculator_steps, operands):
        response = calculator_steps.do_remainder(operands)

        # assert_http_status_code(response=response, expected_code=422)
        assert_json_header(response=response)

        error = CalculatorSchemasSteps.get_calculation_error(response)
        assert_calculator_calculation_error(calculation_error=error)
