"""
Логические шаги сценариев работы с приложением из консоли.
"""

import subprocess
from dataclasses import dataclass

from api.client.utils import get_api_client
from steps.server_api.server_steps import ServerSteps


@dataclass(frozen=True, slots=True)
class ApplicationSteps:
    """
    Логические шаги сценариев работы с приложением из консоли.

    :ivar path: Путь exe файла приложения.
    :ivar host: Хост сервера.
    :ivar port: Порт сервера.
    """

    path: str
    host: str | None = None
    port: str | None = None

    def start(self):
        """
        Запуск приложения.
        """
        command = f'{self.path} start {self.host if self.host else ""} {self.port if self.port else ""}'
        subprocess.run(command)

    def stop(self):
        """
        Остановка приложения.
        """
        command = f'{self.path} stop'
        subprocess.run(command)

    def restart(self):
        """
        Перезапуск приложения.
        """
        command = f'{self.path} restart'
        subprocess.run(command)

    def get_state(self):
        """
        Проверка состояния сервера приложения.
        """
        host = self.host if self.host else 'localhost'
        port = self.port if self.port else '17678'
        client = get_api_client(f'http://{host}:{port}/api')  # ToDo: исправить хардкод
        server_steps = ServerSteps(client)
        return server_steps.do_server_state()
