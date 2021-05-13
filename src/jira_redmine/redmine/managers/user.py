# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.user import User
from jira_redmine.redmine.converter import Converter
from jira_redmine.redmine.managers.base import BaseRedmineManager


class UserManager(BaseRedmineManager):
    """Менеджер доступа к пользователям Redmine."""

    def get_all(self) -> List[User]:
        """Получить всех пользователей."""
        users = self._client.user.all()
        return [
            Converter.get_user(user)
            for user in users
        ]

    def get(self, user_id: Union[int, str]) -> User:
        """Получить пользователя по идентификатору."""
        user_id = int(user_id)
        user = self._get_or_raise('user', user_id, User, manager_method='get')
        return Converter.get_user(user)

    def create(self, user: User) -> User:
        """Создать нового пользователя."""
        raise NotImplementedError
