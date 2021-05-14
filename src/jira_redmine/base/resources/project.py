# coding: utf-8
from jira_redmine.base.resources.base import BaseResource
from jira_redmine.base.resources.user import User
from jira_redmine.base.resources.user import UserDefaultMixin


class Project(UserDefaultMixin, BaseResource):
    """Ресурс проекта."""

    _CAPTION: str = 'проект'

    def __init__(
        self,
        name: str = None,
        description: str = None,
        creator: User = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.creator = creator or self._get_def_user()
