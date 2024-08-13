import allure

from assertions.base_assertions import assert_http_status_code, assert_json_header
from assertions.server_assertions import assert_server_state
from steps.server.server_steps import ServerSteps


@allure.epic('Сервер')
@allure.feature('Состояние сервера')
class TestServer:

    @allure.story('Состояние сервера')
    @allure.title('Состояние сервера - запущен')
    def test_server_state(self, server_steps):
        response = server_steps.do_server_state()
        assert_http_status_code(response=response, expected_code=200)
        assert_json_header(response=response)

        state = ServerSteps.get_server_state(response)
        assert_server_state(server_state=state)
