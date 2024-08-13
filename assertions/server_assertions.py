from assertions.base_assertions import assert_internal_status_code
from models.server_state import ServerState


def assert_server_state(server_state: ServerState):
    """
    Проверяет состояние сервера.

    :param server_state: Состояние сервера.
    """

    assert_internal_status_code(server_state, 0)
    assert server_state.state == 'OK'

