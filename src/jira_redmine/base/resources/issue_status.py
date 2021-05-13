# coding: utf-8
from jira_redmine.base.resources.base import BaseResource


class IssueStatus(BaseResource):
    """Ресурс статуса задач."""

    _CAPTION: str = 'статус задачи'

    def __init__(self, name: str = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
