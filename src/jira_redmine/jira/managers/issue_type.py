# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.issue_type import IssueType
from jira_redmine.jira.converter import Converter
from jira_redmine.jira.managers.base import BaseJiraManager


class IssueTypeManager(BaseJiraManager):
    """Менеджер доступа к типам задач Jira."""

    def get_all(self) -> List[IssueType]:
        """Получить все типы задач по проекту."""
        issue_types = self._client.issue_types()
        return [
            Converter.get_issue_type(issue_type)
            for issue_type in issue_types
        ]

    def get(self, issue_type_id: Union[int, str]) -> IssueType:
        """Получить тип задачи по идентификатору."""
        # TODO ? issue_type_by_name
        issue_type = self._get_or_raise('issue_type', issue_type_id, IssueType)
        return Converter.get_issue_type(issue_type)

    def create(self, **kwargs):
        """Создать новый тип звдачи."""
        # return self._client.create_issue_type(**kwargs)
