import allure
import pytest

from assertions.base_assertions import assert_http_status_code, assert_connection_error
from tests.utils import idfn


@pytest.fixture(scope='session', autouse=True)
def prepare_application():
    """
    Отключение автоматического запуска приложения.
    """
    pass


@allure.epic('Приложение')
@allure.feature('Управление приложением из консоли')
class TestApplication:

    @allure.story('Запуск приложение')
    @pytest.mark.parametrize('application_steps',
                             [(None, None),
                              ('127.10.5.3', None),
                              ('127.0.0.1', '65432'),
                              ('localhost', '17678')],
                             indirect=True,
                             ids=idfn)
    def test_start_application(self, application_steps):
        response = application_steps.get_state()

        assert_http_status_code(response=response, expected_code=200)

    @allure.story('Остановка приложение')
    def test_stop_application(self, application_steps):
        application_steps.stop()  # ToDo: Фикстура повторно вызывает stop. Мб добавить флаг на проверку работы

        with assert_connection_error():
            application_steps.get_state()

    @allure.story('Перезапуск приложение')
    @pytest.mark.parametrize('application_steps',
                             [(None, None),
                              ('127.2.2.2', None),
                              ('127.10.10.3', 65432)],
                             indirect=True,
                             ids=idfn)
    def test_restart_application(self, application_steps):
        response = application_steps.get_state()
        assert_http_status_code(response=response, expected_code=200)

        application_steps.restart()

        response = application_steps.get_state()
        assert_http_status_code(response=response, expected_code=200)
