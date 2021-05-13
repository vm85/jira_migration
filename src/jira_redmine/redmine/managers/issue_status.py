# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.issue_status import IssueStatus
from jira_redmine.redmine.converter import Converter
from jira_redmine.redmine.managers.base import BaseRedmineManager


class IssueStatusManager(BaseRedmineManager):
    """Менеджер доступа к статусам задач Redmine."""

    def get_all(self) -> List[IssueStatus]:
        """Получить все статусы задач."""
        issue_statuses = self._client.issue_status.all()
        return [
            Converter.get_issue_status(issue_status)
            for issue_status in issue_statuses
        ]

    def get(self, issue_status_id: Union[int, str]) -> IssueStatus:
        """Получить тип задачи по идентификатору."""
        issue_status_id = int(issue_status_id)
        issue_status = self._get_or_raise(
            'issue_status', issue_status_id, IssueStatus, manager_method='get'
        )
        return Converter.get_issue_status(issue_status)

    def create(self, issue_status: IssueStatus) -> IssueStatus:
        """Создать новый тип звдачи."""
        raise NotImplementedError
