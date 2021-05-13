# coding: utf-8
from abc import ABC
from abc import abstractmethod
from typing import Union

from jira.resources import Issue as JiraIssue
from jira.resources import IssueType as JiraIssueType
from jira.resources import Project as JiraProject
from jira.resources import Status as JiraIssueStatus
from jira.resources import User as JiraUser
from redminelib.resources import Issue as RedmineIssue
from redminelib.resources import IssueStatus as RedmineIssueStatus
from redminelib.resources import Project as RedmineProject
from redminelib.resources import Tracker as RedmineIssueType
from redminelib.resources import User as RedmineUser

from jira_redmine.base.resources.issue import Issue
from jira_redmine.base.resources.issue_status import IssueStatus
from jira_redmine.base.resources.issue_type import IssueType
from jira_redmine.base.resources.project import Project
from jira_redmine.base.resources.user import User


class BaseConverter(ABC):
    """Класс-преобразователь из ресурса клиента в локальный ресурс."""

    @classmethod
    @abstractmethod
    def get_user(cls, user: Union[JiraUser, RedmineUser]) -> User:
        """Преобразование пользователя Jira в локального пользователя."""

    @classmethod
    @abstractmethod
    def get_issue_status(
        cls,
        status: Union[JiraIssueStatus, RedmineIssueStatus]
    ) -> IssueStatus:
        """Преобразование статуса задачс Jira в локальный статус задачи."""

    @classmethod
    @abstractmethod
    def get_issue_type(
        cls,
        issue_type: Union[JiraIssueType, RedmineIssueType]
    ) -> IssueType:
        """Преобразование типа задачи Jira в локальный тип задачи."""

    @classmethod
    @abstractmethod
    def get_project(
        cls,
        project: Union[JiraProject, RedmineProject]
    ) -> Project:
        """Преобразование проекта Jira в локальный проект."""

    @classmethod
    @abstractmethod
    def get_issue(cls, issue: Union[JiraIssue, RedmineIssue]) -> Issue:
        """Преобразование задачи Jira в локальную задачу."""
