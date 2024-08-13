import pytest

from api.client.utils import get_api_client
from steps.calculator.calculator_schemas_steps import CalculatorSchemasSteps
from steps.calculator.calculator_steps import CalculatorSteps
from steps.server.server_schemas_steps import ServerSchemasSteps
from steps.server.server_steps import ServerSteps


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
