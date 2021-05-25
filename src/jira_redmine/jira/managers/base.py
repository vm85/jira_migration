# coding: utf-8
from abc import ABC
from http import HTTPStatus
from typing import Type
from typing import Union

from jira.exceptions import JIRAError
from jira.resources import Issue as JiraIssue
from jira.resources import IssueType as JiraIssueType
from jira.resources import Project as JiraProject
from jira.resources import Status as JiraIssueStatus
from jira.resources import User as JiraUser

from jira_redmine.base.manager import BaseManager
from jira_redmine.base.resources.base import BaseResource


class BaseJiraManager(BaseManager, ABC):
    """Базовый менеджер доступа к данным Jira."""

    def _get_or_raise(
        self,
        manager_name: str,
        resource_id: Union[int, str],
        resource_class: Type[BaseResource],
        **kwargs
    ) -> Union[
        JiraUser, JiraProject, JiraIssueStatus, JiraIssueType, JiraIssue
    ]:
        """Получить ресурс или выдать ошибку отсутствия ресурса Jira."""
        return super()._get_or_raise(
            manager_name,
            resource_id,
            resource_class,
            exceptions=JIRAError,
            obj_not_exists_checker=(
                lambda e: e.status_code == HTTPStatus.NOT_FOUND
            ),
        )
