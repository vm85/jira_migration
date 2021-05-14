# coding: utf-8
from jira_redmine.base.resources.base import BaseResource
from jira_redmine.settings import DEFAULT_USER


class User(BaseResource):
    """Ресурс пользователя."""

    _CAPTION: str = 'пользователь'

    def __init__(self, name: str = None, email: str = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email


class UserDefaultMixin:
    """Миксин возвращающий ресурс пользователя по умолчанию."""

    __def_user = None

    def _get_def_user(self):
        """Ресурс пользователя по умолчанию."""
        if not self.__def_user:
            self.__def_user = User(
                resource_id=DEFAULT_USER['ID'],
                name=DEFAULT_USER['NAME'],
            )
        return self.__def_user
