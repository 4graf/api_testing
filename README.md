# api_testing
Тестовое задание на ***QA Python***.

> Реализованы автотесты, проверяющие API WEB приложения *webcalculator* и запуск его сервера из консоли.

## Описание переменных окружения:

- **BASE_URL** - базовый URL сервера
- **STATE** - эндпоинт для проверки состояния сервера
- **ADDITION** - эндпоинт для сложения двух чисел 
- **MULTIPLICATION** - эндпоинт для умножения двух чисел
- **DIVISION** - эндпоинт для целочисленного деления двух чисел
- **REMAINDER** - эндпоинт для вычисления остатка от деления двух чисел
- **EXE_PATH** - путь к исполняемому файлу приложения webcalculator.exe

## Запуск тестов через Docker:

Пока не реализовано :)

## Ручной запуск тестов:

1. Установить `Python 3.12`
2. Установить зависимости из `requirements.txt`
3. Создать файл `env` с перечисленными переменными окружения
4. Запустить тесты командой `pytest` из корневой папки проекта.

## Просмотр журнала тестов:

Для просмотра Allure журнала тестов необходимо выполнить команду `allure serve allure-results` 
из корневой папки проекта.
