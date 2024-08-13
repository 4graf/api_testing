from httpx import Response
from pydantic import BaseModel


def assert_http_status_code(response: Response, expected_code: int):
    """
    Проверяет код ответа на запрос с ожидаемым кодом.

    :param response: Ответ от сервера на запрос
    :param expected_code: Ожидаемый код ответа запроса
    """

    assert response.status_code == expected_code


def assert_json_header(response: Response):
    """
    Проверяет заголовки ответа на запрос с json.

    :param response: Ответ от сервера на запрос.
    """

    assert response.headers['Content-Type'] == 'application/json'


def assert_header_access_method(response: Response, expected_methods: str):
    """
    Проверяет заголовки ответа на запрос с json.

    :param response: Ответ от сервера на запрос.
    :param expected_methods: Ожидаемые разрешённые методы.
    """

    assert response.headers['Access-Control-Request-Method'] == expected_methods


def assert_internal_status_code(data: BaseModel, expected_status_code):
    assert data.status_code == expected_status_code


def assert_schema(response: Response, expected_schema: type[BaseModel]):
    """
    Проверяет схему тела ответа с ожидаемой схемой.

    :param response: Ответ от сервера на запрос.
    :param expected_schema: Ожидаемая схема ответа.
    :raises ValidationError: Вызывается, когда тело ответа не соответствует ожидаемой схеме
    """
    body = response.json()
    expected_schema.model_validate(body, strict=True)
