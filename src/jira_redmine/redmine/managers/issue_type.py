# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.issue_type import IssueType
from jira_redmine.redmine.converter import Converter
from jira_redmine.redmine.managers.base import BaseRedmineManager


class IssueTypeManager(BaseRedmineManager):
    """Менеджер доступа к типам задач Redmine."""

    def get_all(self) -> List[IssueType]:
        """Получить все типы задач."""
        issue_types = self._client.tracker.all()
        return [
            Converter.get_issue_type(issue_type)
            for issue_type in issue_types
        ]

    def get(self, issue_type_id: Union[int, str]) -> IssueType:
        """Получить тип задачи по идентификатору."""
        issue_type_id = int(issue_type_id)
        issue_type = self._get_or_raise(
            'tracker', issue_type_id, IssueType, manager_method='get'
        )
        return Converter.get_issue_type(issue_type)

    def create(self, issue_type: IssueType) -> IssueType:
        """Создать новый тип звдачи."""
        raise NotImplementedError
