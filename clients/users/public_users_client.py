from typing import TypedDict
import httpx import Response

from clients.api_client import APIClient


class CreateUserRequest(TypedDict):
    """Структура запроса для создания пользователя."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами пользователей (/api/v1/users),
    которые не требуют авторизации.
    """

    def create_user_api(self, request: CreateUserRequest) -> httpx.Response:
        """
        Метод создает пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)