# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.issue import Issue
from jira_redmine.jira.converter import Converter
from jira_redmine.jira.managers.base import BaseJiraManager


class IssueManager(BaseJiraManager):
    """Менеджер доступа к задачам Jira."""

    def get_all(self, project_id: Union[int, str]) -> List[Issue]:
        """Получить все задачи по проекту."""
        issues = self._client.search_issues(f'project = "{project_id}"')
        return [Converter.get_issue(issue) for issue in issues]

    def get(self, issue_id: Union[int, str]) -> Issue:
        """Получить задачу по идентификатору."""
        issue = self._get_or_raise('issue', issue_id, Issue)
        return Converter.get_issue(issue)

    def create(self, issue: Issue) -> Issue:
        """Создать новую звдачу."""
        jira_issue = self._client.create_issue(
            project=issue.project.key,
            summary=issue.subject,
            description=issue.description,
            issuetype={'id': issue.issue_type.key},
            assignee={'id': issue.assignee.key} if issue.assignee else None,
            reporter={'id': issue.creator.key},
            # created=issue.created,
        )
        self.update_status(issue)
        return self.get(jira_issue.key)

    def update_status(self, issue: Issue) -> Issue:
        """Обновление статуса задачи."""
        self._client.transition_issue(issue.key, issue.status.name)
        return issue

    def update(self, issue: Issue) -> Issue:
        """Обновление задачи."""
        raise NotImplementedError
