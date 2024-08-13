import allure
import pytest

from assertions.base_assertions import assert_http_status_code, assert_json_header, assert_header_access_method
from assertions.calculator_assertions import assert_internal_status_code
from models.calculator.numeric_operands import IntegerOperands
from tests.utils import idfn


@allure.epic('Сервер')
@allure.feature('Форматы схем ответов о состоянии сервера')
class TestServerSchemas:
    @staticmethod
    def get_data_example():
        return IntegerOperands(x=5, y=2)

    @allure.story('Состояние сервера с разными HTTP методами')
    @allure.title('POST Состояние сервера')
    @pytest.mark.parametrize("payload",
                             [get_data_example(),
                              None],
                             ids=idfn)
    def test_state_post_with_payload(self, server_schemas_steps, payload):
        response = server_schemas_steps.send_request_to_state(method='post', payload=payload)

        # assert_http_status_code(response, 422)
        assert_json_header(response=response)

        result = server_schemas_steps.get_server_error(response)
        assert_internal_status_code(result, 5)

    @allure.story('Состояние сервера с разными HTTP методами')
    @allure.title('GET Состояние сервера')
    @pytest.mark.parametrize("payload",
                             [get_data_example(),
                              None],
                             ids=idfn)
    def test_state_get_with_payload(self, server_schemas_steps, payload):
        response = server_schemas_steps.send_request_to_state(method='get', payload=payload)

        assert_http_status_code(response, 200)
        assert_json_header(response=response)

        result = server_schemas_steps.get_server_state(response)
        assert_internal_status_code(result, 0)

    @allure.story('Состояние сервера с разными HTTP методами')
    @allure.title('OPTIONS Состояние сервера')
    @pytest.mark.parametrize("payload",
                             [get_data_example(),
                              None],
                             ids=idfn)
    def test_state_options(self, server_schemas_steps, payload):
        response = server_schemas_steps.send_request_to_state(method='options', payload=payload)

        assert_http_status_code(response, 200)
        assert_header_access_method(response=response, expected_methods='POST, GET, OPTIONS')

    @allure.story('Состояние сервера с разными HTTP методами')
    @allure.title('DELETE Состояние сервера')
    @pytest.mark.parametrize("payload",
                             [get_data_example(),
                              None],
                             ids=idfn)
    def test_state_delete(self, server_schemas_steps, payload):
        response = server_schemas_steps.send_request_to_state(method='delete', payload=payload)

        assert_http_status_code(response, 501)
