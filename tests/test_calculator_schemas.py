import allure
import pytest

from assertions.base_assertions import assert_http_status_code, assert_json_header, assert_header_access_method
from assertions.calculator_assertions import assert_internal_status_code
from models.calculator.numeric_operands import IntegerOperands
from tests.utils import idfn


@allure.epic('Калькулятор')
@allure.feature('Форматы схем ответов калькулятора')
class TestCalculatorSchemas:
    @staticmethod
    def get_operands_example():
        return IntegerOperands(x=5, y=2)

    @allure.story('Состояние сервера с разными HTTP методами')
    @allure.title('POST Состояние сервера')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_state_post_with_payload(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_state(method='post', payload=payload)

        # assert_http_status_code(response, 422)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Состояние сервера с разными HTTP методами')
    @allure.title('GET Состояние сервера')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_state_get_with_payload(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_state(method='get', payload=payload)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_server_state(response)
        assert_internal_status_code(result, 0)

    @allure.story('Состояние сервера с разными HTTP методами')
    @allure.title('OPTIONS Состояние сервера')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_state_options(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_state(method='options', payload=payload)

        assert_http_status_code(response, 200)
        assert_header_access_method(response=response, expected_methods='POST, GET, OPTIONS')

    @allure.story('Состояние сервера с разными HTTP методами')
    @allure.title('DELETE Состояние сервера')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_state_delete(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_state(method='delete', payload=payload)

        assert_http_status_code(response, 501)

    @allure.story('Сложение с разными HTTP методами')
    @allure.title('POST сложение с данными')
    def test_addition_post_with_payload(self, calculator_schemas_steps):
        operands = self.get_operands_example()

        response = calculator_schemas_steps.send_request_to_addition(method='post', payload=operands)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_result(response)
        assert_internal_status_code(result, 0)

    @allure.story('Сложение с разными HTTP методами')
    @allure.title('POST сложение без данных')
    def test_addition_post_without_payload(self, calculator_schemas_steps):
        response = calculator_schemas_steps.send_request_to_addition(method='post')

        # assert_http_status_code(response, 422)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Сложение с разными HTTP методами')
    @allure.title('GET сложение')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_addition_get_with_payload(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_addition(method='get', payload=payload)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Сложение с разными HTTP методами')
    @allure.title('OPTIONS сложение')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_addition_options(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_addition(method='options', payload=payload)

        assert_http_status_code(response, 200)
        assert_header_access_method(response=response, expected_methods='POST, GET, OPTIONS')

    @allure.story('Сложение с разными HTTP методами')
    @allure.title('DELETE сложение')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_addition_delete(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_addition(method='delete', payload=payload)

        assert_http_status_code(response, 501)

    @allure.story('Умножение с разными HTTP методами')
    @allure.title('POST Умножение с данными')
    def test_multiplication_post_with_payload(self, calculator_schemas_steps):
        operands = self.get_operands_example()

        response = calculator_schemas_steps.send_request_to_multiplication(method='post', payload=operands)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_result(response)
        assert_internal_status_code(result, 0)

    @allure.story('Умножение с разными HTTP методами')
    @allure.title('POST Умножение без данных')
    def test_multiplication_post_without_payload(self, calculator_schemas_steps):
        response = calculator_schemas_steps.send_request_to_multiplication(method='post')

        # assert_http_status_code(response, 422)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Умножение с разными HTTP методами')
    @allure.title('GET Умножение')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_multiplication_get_with_payload(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_multiplication(method='get', payload=payload)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Умножение с разными HTTP методами')
    @allure.title('OPTIONS Умножение')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_multiplication_options(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_multiplication(method='options', payload=payload)

        assert_http_status_code(response, 200)
        assert_header_access_method(response=response, expected_methods='POST, GET, OPTIONS')

    @allure.story('Умножение с разными HTTP методами')
    @allure.title('DELETE Умножение')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_multiplication_delete(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_multiplication(method='delete', payload=payload)

        assert_http_status_code(response, 501)

    @allure.story('Целочисленное деление с разными HTTP методами')
    @allure.title('POST Целочисленное деление с данными')
    def test_division_post_with_payload(self, calculator_schemas_steps):
        operands = self.get_operands_example()

        response = calculator_schemas_steps.send_request_to_division(method='post', payload=operands)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_result(response)
        assert_internal_status_code(result, 0)

    @allure.story('Целочисленное деление с разными HTTP методами')
    @allure.title('POST Целочисленное деление без данных')
    def test_division_post_without_payload(self, calculator_schemas_steps):
        response = calculator_schemas_steps.send_request_to_division(method='post')

        # assert_http_status_code(response, 422)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Целочисленное деление с разными HTTP методами')
    @allure.title('GET Целочисленное деление')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_division_get_with_payload(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_division(method='get', payload=payload)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Целочисленное деление с разными HTTP методами')
    @allure.title('OPTIONS Целочисленное деление')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_division_options(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_division(method='options', payload=payload)

        assert_http_status_code(response, 200)
        assert_header_access_method(response=response, expected_methods='POST, GET, OPTIONS')

    @allure.story('Целочисленное деление с разными HTTP методами')
    @allure.title('DELETE Целочисленное деление')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_division_delete(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_division(method='delete', payload=payload)

        assert_http_status_code(response, 501)

    @allure.story('Вычисление остатка от деления с разными HTTP методами')
    @allure.title('POST Вычисление остатка от деления с данными')
    def test_remainder_post_with_payload(self, calculator_schemas_steps):
        operands = self.get_operands_example()

        response = calculator_schemas_steps.send_request_to_remainder(method='post', payload=operands)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_result(response)
        assert_internal_status_code(result, 0)

    @allure.story('Вычисление остатка от деления с разными HTTP методами')
    @allure.title('POST Вычисление остатка от деления без данных')
    def test_remainder_post_without_payload(self, calculator_schemas_steps):
        response = calculator_schemas_steps.send_request_to_remainder(method='post')

        # assert_http_status_code(response, 422)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Вычисление остатка от деления с разными HTTP методами')
    @allure.title('GET Вычисление остатка от деления')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_remainder_get_with_payload(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_remainder(method='get', payload=payload)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = calculator_schemas_steps.get_calculation_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Вычисление остатка от деления с разными HTTP методами')
    @allure.title('OPTIONS Вычисление остатка от деления')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_remainder_options(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_remainder(method='options', payload=payload)

        assert_http_status_code(response, 200)
        assert_header_access_method(response=response, expected_methods='POST, GET, OPTIONS')

    @allure.story('Вычисление остатка от деления с разными HTTP методами')
    @allure.title('DELETE Вычисление остатка от деления')
    @pytest.mark.parametrize("payload",
                             [get_operands_example(),
                              None],
                             ids=idfn)
    def test_remainder_delete(self, calculator_schemas_steps, payload):
        response = calculator_schemas_steps.send_request_to_remainder(method='delete', payload=payload)

        assert_http_status_code(response, 501)
