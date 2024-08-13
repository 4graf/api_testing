import pytest

from api.client.utils import get_api_client
from settings import ApplicationSettings
from steps.application.application_steps import ApplicationSteps
from steps.calculator_api.calculator_schemas_steps import CalculatorSchemasSteps
from steps.calculator_api.calculator_steps import CalculatorSteps
from steps.server_api.server_schemas_steps import ServerSchemasSteps
from steps.server_api.server_steps import ServerSteps

application_settings = ApplicationSettings()


@pytest.fixture(scope='session', autouse=True)
def prepare_application():
    application_steps = ApplicationSteps(path=application_settings.exe_path)
    application_steps.start()

    yield

    application_steps.stop()


@pytest.fixture(scope='session')
def api_client():
    client = get_api_client()
    yield client
    client.close()


@pytest.fixture(scope='session')
def calculator_steps(api_client):
    yield CalculatorSteps(api_client)


@pytest.fixture(scope='session')
def calculator_schemas_steps(api_client):
    yield CalculatorSchemasSteps(api_client)


@pytest.fixture(scope='session')
def server_steps(api_client):
    yield ServerSteps(api_client)


@pytest.fixture(scope='session')
def server_schemas_steps(api_client):
    yield ServerSchemasSteps(api_client)


@pytest.fixture(scope='session')
def application_steps(request) -> ApplicationSteps:
    if hasattr(request, 'param'):
        host, port = request.param
    else:
        host, port = None, None
    application_steps = ApplicationSteps(path=application_settings.exe_path, host=host, port=port)
    application_steps.start()

    yield application_steps

    application_steps.stop()
