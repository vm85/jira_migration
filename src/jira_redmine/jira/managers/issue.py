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
        project = issue.fields.project
        return Issue(
            resource_id=issue.id,
            key=issue.key,
            subject=issue.fields.summary,
            description=issue.fields.description,
            project=Project(
                resource_id=project.id,
                key=project.key,
                name=project.name,
                # TODO разобраться почему нет описания в all
                description=getattr(project, 'description', ''),
            )
        )

    def all(self, project_id: Union[int, str]) -> List[Issue]:
        """"""
        issues = self._client.search_issues(f'project = "{project_id}"')
        return [self._get_issue(issue) for issue in issues]

    def get(self, issue_id: Union[int, str]) -> Issue:
        """"""
        issue = self._client.issue(issue_id)
        return self._get_issue(issue)
