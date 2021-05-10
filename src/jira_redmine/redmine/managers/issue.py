# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.manager import BaseManager
from jira_redmine.base.resources.issue import Issue
from jira_redmine.base.resources.project import Project


class IssueManager(BaseManager):
    """"""

    @staticmethod
    def _get_issue(issue):
        """"""
        project = issue.project
        return Issue(
            resource_id=issue.id,
            key=issue.id,
            subject=issue.subject,
            description=issue.description,
            project=Project(
                resource_id=project.id,
                # TODO разобраться почему нет поля
                key=getattr(project, 'identifier', ''),
                name=project.name,
                # TODO разобраться почему нет описания
                description=getattr(project, 'description', ''),
            )
        )

    def all(self, project_id: Union[int, str]) -> List[Issue]:
        """"""
        project = self._client.project.get(project_id)
        issues = project.issues
        return [self._get_issue(issue) for issue in issues]

    def get(self, issue_id: Union[int, str]) -> Issue:
        """"""
        issue = self._client.issue.get(issue_id)
        return self._get_issue(issue)
