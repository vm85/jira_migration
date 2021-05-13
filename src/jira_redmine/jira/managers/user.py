# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.user import User
from jira_redmine.jira.converter import Converter
from jira_redmine.jira.managers.base import BaseJiraManager


class UserManager(BaseJiraManager):
    """Менеджер доступа к пользователям Jira."""

    def get_all(self) -> List[User]:
        """Получить всех пользователей."""
        raise NotImplementedError

    def get(self, user_id: Union[int, str]) -> User:
        """Получить пользователя по идентификатору."""
        user_id = int(user_id)
        user = self._get_or_raise('user', user_id, User)
        return Converter.get_user(user)

    def create(self, user: User) -> User:
        """Создать нового пользователя."""
        raise NotImplementedError
