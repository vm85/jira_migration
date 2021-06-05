# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.issue import Issue
from jira_redmine.redmine.converter import Converter
from jira_redmine.redmine.managers.base import BaseRedmineManager


class IssueManager(BaseRedmineManager):
    """Менеджер доступа к задачам Redmine."""

    def get_all(self, project_id: Union[int, str]) -> List[Issue]:
        """Получить все задачи по проекту."""
        project = self._client.project.get(project_id)
        issues = project.issues
        return [Converter.get_issue(issue) for issue in issues]

    def get(self, issue_id: Union[int, str]) -> Issue:
        """Получить задачу по идентификатору."""
        issue = self._get_or_raise(
            'issue', issue_id, Issue, manager_method='get'
        )
        return Converter.get_issue(issue)

    def create(self, issue: Issue) -> Issue:
        """Создать новую звдачу."""
        raise NotImplementedError
        # issue = self._client.issue.create(
        #     # project_id='vacation',
        #     # subject='Vacation',
        #     # tracker_id=8,
        #     # description='foo',
        #     # status_id=3,
        #     # priority_id=7,
        #     # assigned_to_id=123,
        #     # watcher_user_ids=[123],
        #     # parent_issue_id=345,
        #     # start_date=datetime.date(2014, 1, 1),
        #     # due_date=datetime.date(2014, 2, 1),
        #     # estimated_hours=4,
        #     # done_ratio=40,
        #     # custom_fields=[
        #     #     {'id': 1, 'value': 'foo'},
        #     #     {'id': 2, 'value': 'bar'}
        #     # ],
        #     # uploads=[
        #     #     {'path': '/absolute/path/to/file'},
        #     #     {'path': BytesIO(b'I am content of file 2')}
        #     # ]
        # )
        # return Converter.get_issue(issue)

    def update(self, issue: Issue, **fields):
        """Обновление задачи."""
        self._client.issue.update(issue.key, **fields)
        return self.get(issue.key)
