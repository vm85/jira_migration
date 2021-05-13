# coding: utf-8
from typing import Union

from redminelib.resources import Issue as RedmineIssue
from redminelib.resources import IssueStatus as RedmineIssueStatus
from redminelib.resources import Project as RedmineProject
from redminelib.resources import Tracker as RedmineIssueType
from redminelib.resources import User as RedmineUser

from jira_redmine.base.converter import BaseConverter
from jira_redmine.base.resources.issue import Issue
from jira_redmine.base.resources.issue_status import IssueStatus
from jira_redmine.base.resources.issue_type import IssueType
from jira_redmine.base.resources.project import Project
from jira_redmine.base.resources.user import User


class Converter(BaseConverter):
    """Класс-преобразователь из ресурса Redmine в локальный ресурс."""

    @classmethod
    def get_user(cls, user: Union[RedmineUser, None]) -> Union[User, None]:
        """Преобразование пользователя Redmine в локального пользователя."""
        if not user:
            return

        name = getattr(user, 'name', None)
        full_name = ' '.join([
            getattr(user, 'firstname', ''),
            getattr(user, 'lastname', '')
        ])
        return User(
            resource_id=str(user.id),
            name=name or full_name,
            # TODO нет поля
            email=getattr(user, 'email', None) or getattr(user, 'mail', None)
        )

    @classmethod
    def get_issue_status(cls, status: RedmineIssueStatus) -> IssueStatus:
        """Преобразование статуса задачс Redmine в локальный статус задачи."""
        # TODO status mapper
        return IssueStatus(
            resource_id=str(status.id),
            name=status.name,
        )

    @classmethod
    def get_issue_type(cls, issue_type: RedmineIssueType) -> IssueType:
        """Преобразование типа задачи Redmine в локальный тип задачи."""
        # TODO mapper
        return IssueType(
            resource_id=str(issue_type.id),
            name=issue_type.name,
        )

    @classmethod
    def get_project(cls, project: RedmineProject) -> Project:
        """Преобразование проекта Redmine в локальный проект."""
        # TODO разобраться почему нет полей
        return Project(
            resource_id=str(project.id),
            key=str(getattr(project, 'identifier', '')),
            name=project.name,
            description=getattr(project, 'description', ''),
            creator=None,  # TODO
        )

    @classmethod
    def get_issue(cls, issue: RedmineIssue) -> Issue:
        """Преобразование задачи Redmine в локальную задачу."""
        project = issue.project
        return Issue(
            resource_id=str(issue.id),
            subject=issue.subject,
            description=issue.description,
            project=cls.get_project(project),
            created=issue.created_on,
            creator=cls.get_user(issue.author),
            issue_type=cls.get_issue_type(issue.tracker),
            status=cls.get_issue_status(issue.status),
            assignee=cls.get_user(getattr(issue, 'assigned_to', None))
        )
