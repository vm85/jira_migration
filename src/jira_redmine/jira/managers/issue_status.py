# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.issue_status import IssueStatus
from jira_redmine.jira.converter import Converter
from jira_redmine.jira.managers.base import BaseJiraManager


class IssueStatusManager(BaseJiraManager):
    """Менеджер доступа к статусам задач Jira."""

    def get_all(self) -> List[IssueStatus]:
        """Получить все статусы задач."""
        issue_statuses = self._client.statuses()
        return [
            Converter.get_issue_status(issue_status)
            for issue_status in issue_statuses
        ]

    def get(self, issue_status_id: Union[int, str]) -> IssueStatus:
        """Получить статус задачи по идентификатору."""
        issue_status = self._get_or_raise(
            'status', issue_status_id, IssueStatus
        )
        return Converter.get_issue_status(issue_status)

    def create(self, **kwargs):
        """Создать новый статус звдачи."""
